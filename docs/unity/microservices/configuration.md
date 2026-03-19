# Microservice configuration

## Overview

Configure microservice build and deployment settings through the Unity Editor. The microservice configuration controls how your services are built, deployed, and managed within the Beamable ecosystem.

## Prerequisites

You need:
- Unity project with Beamable package installed
- Microservices created in your project
- Access to Unity Editor preferences

## Steps

1. Open Unity Editor
2. Navigate to **Window > Beamable > Configuration**
3. Select the **Microservices** tab
4. Configure your settings
5. Apply changes

## Configuration options

### Build settings

Configure how microservices are built and compiled.

#### Auto-generate client code

Control automatic client code generation for each service:

- **Enabled**: Client code generates automatically when service builds
- **Disabled**: Manual client code generation required

#### Parallel build count

Set the maximum number of services that build simultaneously:

- **Default**: 8 parallel builds
- **Custom**: Set specific limit for your machine's resources
- **Disabled**: No limit (uses system default)

### Deployment settings

#### Health checks

Configure pre-deployment health validation:

- **Enabled**: Run health checks before publishing
- **Disabled**: Skip health check validation

#### Merge deployments

Control deployment behavior for existing services:

- **Merge**: Preserve existing remote services not present locally  
- **Replace**: Remove remote services that don't exist locally

## Examples

### Memory-constrained setup

For machines with limited resources:

1. Set **Max Parallel Build Count** to `2`
2. Enable **Sequential Build** option
3. This prevents out-of-memory issues during builds

### Development environment

For active development:

1. Enable **Auto Generate Client** for all services
2. Set **Max Parallel Build Count** to `4`
3. Enable **Health Checks** for deployment validation

### Production deployment

For production releases:

1. Disable **Auto Generate Client** for stable services
2. Use default **Max Parallel Build Count** (`8`)
3. Enable **Health Checks** for deployment safety

## Notes

- Lower parallel build counts reduce memory usage but increase build time
- Auto-generated client code updates automatically when services change
- Health checks add deployment time but improve reliability
- Configuration changes apply to future builds and deployments

*This documentation reflects changes from PR #4538.*