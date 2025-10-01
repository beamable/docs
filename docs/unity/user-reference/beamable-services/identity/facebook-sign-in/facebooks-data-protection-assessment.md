---
title: "Facebook's Data Protection Assessment"
slug: "facebooks-data-protection-assessment"
excerpt: ""
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed May 31 2023 19:45:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Oct 25 2023 20:56:57 GMT+0000 (Coordinated Universal Time)"
---
If you implement Facebook sign-in, you might be asked to submit an annual Data Protection Assessment through your Facebook Developer account. The following answeres can be used if you have implemented Facebook authentication through Beamable.

> 🚧 By Default, Beamable Does Not Store Facebook Platform Data
> 
> If you are using Facebook auth through Beamable, no Facebook Platform Data is stored of any kind (email, passwork, graph data, etc). The Beamable authentication flow retrieves a revokable, transient auth token. Should the game developer choose to call and store other data, that is outside the standard implementation and the answers to these questions would be invalid. 
> 
> If the game developer chooses to call and store Facebook Platform Data, you do so at your own risk.

# Answers to the Data Protection Assessment

If you have implemented a default Facebook authentication flow using Beamable, you can answer the Data Protection Assessment using the following answers:

## Data Use

- Does the application use Platform data to disadvantage certain people - NO
- Does the application use Platform data to make decisions about housing/employment, etc. - NO
- Does the application use Platform data for surveillance (law or national security) - NO
- How does your software use Platform Data? - Beamable Sign-In transmits the user’s access token to backend services via HTTP request secured by industry standard SSL/TLS, in order to associate a Beamable account with a Facebook/Meta account. The token only exists in memory for the duration of the request and is never stored. The platform-specific account id is stored in order to resolve the player account in the future in case they reinstall the app, or login from a different device

## Data Sharing

- Do you share platform data you receive through this app for any reasons - CHECK "I am not sharing platform data that is received through this app."

## Data Deletion

- Would you delete Platform Data in ALL the following circumstances - YES
- Do you take steps to delete platform data as soon as reasonably possible - YES
- How do you determine when Platform Data is no longer necessary to provide an app experience or service to users? - We only store platform data that is strictly required to deliver feature functionality, and then only upon player opt-in. For instance, a player may opt-into (but is not required to) using Facebook or another social login mechanism to access their player account across devices. In such cases, we may need to store the platform-specific account id in order to locate the player account upon login. A player may either, in a self-service manner, remove this login mechanism or request that the developer do this for them. In such a case, we determine that Platform Data is no longer necessary when the player expresses as much, or the feature is deprecated.
- How can users request their data to be deleted? - Users can contact the developer or Beamable via email, expressing that their data be deleted. Upon receipt of such a request, and verification that the player does indeed own the account, deletion of platform data is a one-click operation via the administrative web portal of the developer.

## Data Security

- Meta requires that you maintain administrative, physical, and technical safeguards that are designed to prevent any unauthorized access, etc. - CHECK "I Understand"
- To answer the following questions, you will need to comprehensively understand how Meta Platform Data related to this app is transmitted, stored, and processed in your software and systems. - CHECK "I Understand"
- Do you have a security certification that meets these critieria (The certification type must be SOC 2, ISO 27001, ISO 27018, or an equivalent) - NO
- Do you store any Meta Platform Data? - CHECK "No, we do not store any Platform Data in either of the cases listed above"
- Do you transmit Meta Platform Data over the internet - NO
- Do you test your app and systems for vulnerabilities and security issues at least every 12 months - YES
- Are Meta API access tokens and app secrets protected? - YES
- Do you test the systems and processes you would use to response to a security incident every 12 months - YES
- Do you require multi-factor authentication for remote access to every account that can connect to your cloud or server environment - YES
- Do you have a system for maintaining accounts - YES
- Do you have a system for keeping system code and environments updated - YES
- Do you have a system in place for logging access to Platform Data and tracing where Platform Data was sent and stored? - YES
- Do you monitor transfers of Platform Data and key points where Platform Data can leave the system (e.g., third parties, public endpoints)? - YES
- Do you have an automated system for monitoring logs and other security events, and to generate alerts for abnormal or security-related events? - YES
- Do you have a publicly available way for people to report security vulnerabilities in this app to you? - YES
- How do you prevent Platform Data from being stored on an organizational or personal device? - All platform data is encrypted in transit and at rest, with the database hosting the data only accessible to the relevant application services. This data is not stored on device, and is only accessible to authorized personnel for the purposes of servicing a customer support request.

## Questions?

If you have questions about these answers or filling our the Data Protection Survey, please email [support@beamable.com](mailto:support@beamable.com).
