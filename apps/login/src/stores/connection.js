import { localStore } from "./localStore";
import { writable, derived } from 'svelte/store';
import {createStandaloneRequester, defaultTokenStorage} from 'beamable-sdk'
import {realmsGetCustomerBasic, realmsGetCustomerAliasAvailableBasic} from 'beamable-sdk/api'

export const beamEnv = localStore('beam-docs-env', 'prod')
export const auth = localStore('beam-docs-auth', {})
export const cid = localStore('beam-docs-cid', '')
export const resolvedCid = localStore('beam-docs-resolved-cid', '')
export const gid = localStore('beam-docs-gid', '')
export const pid = localStore('beam-docs-pid', '')
export const reviewData = localStore('beam-docs-review', {})


export const requester = derived([cid, auth, beamEnv], ([$cid, $auth, $beamEnv]) => {

    const ts = defaultTokenStorage({
        pid: ''
    })
 
    const r = createStandaloneRequester({
        cid: $cid,
        pid: '',
        environment: $beamEnv,
        tokenStorage: ts
    })

    if ($auth.access_token){
        console.log('configuring requester with auth')
        ts.setTokenData({
            accessToken: $auth.access_token,
            refreshToken: $auth.refresh_token,
            expiresIn: $auth.expires_in
        })
    } 
    r.defaultHeaders = {
        'X-BEAM-SCOPE': $cid
    }
    return r;
})


export const customer = derived([requester, auth], ([$requester, $auth], set) => {
    if (!$auth.access_token){
        console.log('there is no valid customer auth, so clearing token')
        set({})
        return;
    }

    realmsGetCustomerBasic($requester).then(data => {
        resolvedCid.set('' + data.body.customer.cid)
        set(data.body)
    }).catch(err => {
        console.error('failed to get customer data', err)
    });
})

export const games = derived([customer], ([$customer]) => {
    if (!$customer || !$customer.customer){
        return []
    }
    // games are realms with no parent
    return $customer.customer.projects.filter(p => !p.parent && !p.archived)
})

export const selectedGame = derived([games, gid], ([$games, $gid]) => {
    if (!$games || $games.length == 0 || !$gid) return {}

    const table = $games.reduce( (agg, curr) => {
        agg[curr.pid] = curr;
        return agg;
    }, {})

    return table[$gid]
})

export const realms = derived([customer, gid], ([$customer, $gid]) => {
    if (!$customer || !$customer.customer){
        return []
    }
    if ($gid.length == 0) return []

    // find all the projects that have the gid in their parent path...
    const nonArchived = $customer.customer.projects.filter(p => !p.archived)

    const table = nonArchived.reduce( (agg, curr) => {
        agg[curr.pid] = curr;
        return agg;
    }, {})
    const realms = nonArchived.filter(p => {

        let maxIter = 9999;
        let curr = p;
        while (maxIter > 0){
            maxIter -= 1

            // console.log('comparing', p.pid, curr.pid, $gid, curr.pid == $gid)
            // base case, this is the target realm.
            if (curr.pid == $gid) return true;

            // base case, there is no parent, so it cannot be part of the game.
            if (!curr.parent) {
                // console.log('no parent')
                return false;
            }

            // recursive case, try going one up the tree. 
            curr = table[curr.parent];
            // console.log('went up', p.parent, curr)
        }
    
        console.error('realm tree is too large', p)
        return false;
    })

    console.log('realms are', realms)
    return realms;
})