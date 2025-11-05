import { mount } from 'svelte'
import App from './App.svelte'

function bind(element, props){
  const app = mount(App, {
    target: element,
    props: {
      gitFragment: props.gitFragment,
      gitCommit: props.gitCommit,
      title: props.title,
      args: props.args
    }
  })
}
export default {
  bind
}