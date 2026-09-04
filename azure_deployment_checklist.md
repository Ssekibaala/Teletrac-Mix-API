# Azure Deployment Checklist

## Pre-Deployment Setup

- [ ] **Install VSCode Extensions**
  - [ ] Azure Account extension
  - [ ] Azure App Service extension
  - [ ] Azure Resources extension (optional)

- [ ] **Azure Account Setup**
  - [ ] Have Azure subscription ready
  - [ ] Login to Azure Portal: https://portal.azure.com
  - [ ] Test VSCode Azure login (Ctrl+Shift+P → "Azure: Sign In")

- [ ] **Application Preparation**
  - [ ] Review `azure_deployment_guide.md`
  - [ ] `app.py` is the production entrypoint (credentials come from App Settings)
  - [ ] Verify `startup.txt` is in project root
  - [ ] Confirm `requirements.txt` has all dependencies
  - [ ] Verify `Procfile` is correct: `web: gunicorn app:app`

## Azure App Service Creation

### Option A: VSCode Method
- [ ] Open Azure Explorer in VSCode
- [ ] Right-click "App Service" → "Create New Web App"
- [ ] Choose subscription
- [ ] Enter unique app name (e.g., `mix-integrate-api-2024`)
- [ ] Select region (closest to users)
- [ ] Select Python 3.12 runtime
- [ ] Choose pricing tier (Free F1 for testing)

### Option B: Azure Portal Method
- [ ] Go to Azure Portal
- [ ] Create → Web App
- [ ] Fill required fields
- [ ] Configure Python 3.12 runtime
- [ ] Create resource group and app service plan

## Security Configuration

- [ ] **Move Credentials to Azure (CRITICAL)**
  - [ ] Navigate to App Service → Configuration → Application settings
  - [ ] Add these environment variables:
    - [ ] `MIX_CLIENT_ID` = `<your-client-id>`
    - [ ] `MIX_CLIENT_SECRET` = `<your-client-secret>`
    - [ ] `MIX_USERNAME` = `<your-username>`
    - [ ] `MIX_PASSWORD` = `<your-password>`
  - [ ] Save and restart app

- [ ] **Code Security**
  - [ ] `app.py` is the production entrypoint
  - [ ] Ensure no hardcoded credentials in deployed code
  - [ ] Verify environment variables are used for credentials

## Deployment Process

- [ ] **Deploy Application**
  - [ ] Right-click project folder in VSCode
  - [ ] Select "Deploy to Web App..."
  - [ ] Choose your created App Service
  - [ ] Wait for deployment to complete

- [ ] **Alternative: Azure CLI**
  - [ ] Install Azure CLI
  - [ ] Run: `az login`
  - [ ] Run: `az webapp deploy --resource-group YourResourceGroup --name YourAppName --src-path . --type zip`

## Post-Deployment Verification

- [ ] **Check Deployment Status**
  - [ ] Go to Azure Portal → App Service
  - [ ] Check deployment status shows "Success"
  - [ ] Note the URL: `https://your-app-name.azurewebsites.net`

- [ ] **Test Basic Functionality**
  - [ ] Visit: `https://your-app-name.azurewebsites.net/health`
  - [ ] Should return: `{"status": "healthy", "app": "Mix Integrate API"}`

- [ ] **Test API Endpoints**
  - [ ] Test: `https://your-app-name.azurewebsites.net/organisations`
  - [ ] Test: `https://your-app-name.azurewebsites.net/sites?organisationIds=123,456`
  - [ ] Verify responses are working correctly

## Monitoring and Troubleshooting

- [ ] **Access Logs**
  - [ ] Azure Portal → App Service → Log stream
  - [ ] VSCode: Right-click App Service → View Logs
  - [ ] Check for any error messages

- [ ] **Application Insights (Optional)**
  - [ ] Enable during app creation or add later
  - [ ] Monitor performance and errors
  - [ ] Set up alerts for issues

## Final Steps

- [ ] **Environment Settings**
  - [ ] Go to Configuration in Azure Portal
  - [ ] Add these settings if not done:
    - [ ] `FLASK_ENV` = `production`
    - [ ] `PYTHONPATH` = `/home/site/wwwroot`

- [ ] **Scale and Performance**
  - [ ] Test under load
  - [ ] Consider scaling up if needed
  - [ ] Monitor costs in Azure Portal

- [ ] **Custom Domain (Optional)**
  - [ ] Configure custom domain if needed
  - [ ] Update DNS records as instructed

## Security Checklist

- [ ] **Production Security**
  - [ ] No hardcoded credentials in code
  - [ ] HTTPS enabled (default in Azure)
  - [ ] Environment variables used for secrets
  - [ ] Consider adding authentication/authorization
  - [ ] Review and implement rate limiting

## Cost Management

- [ ] **Monitor Usage**
  - [ ] Check Azure Portal for usage metrics
  - [ ] Set up billing alerts
  - [ ] Use Free tier (F1) for development
  - [ ] Scale appropriately for production

## Documentation

- [ ] **Save Important Information**
  - [ ] App Service URL
  - [ ] Resource group name
  - [ ] App service plan details
  - [ ] Azure subscription details
  - [ ] Any custom domains configured

## Success Criteria

✅ **Deployment is successful when:**
- [ ] App Service status shows "Running"
- [ ] `/health` endpoint returns healthy status
- [ ] At least one API endpoint works correctly
- [ ] No critical errors in logs
- [ ] Application is accessible via public URL

## Troubleshooting Common Issues

### Import Errors
- [ ] Check all dependencies in `requirements.txt`
- [ ] Verify Python version compatibility

### Startup Failures
- [ ] Check `Procfile` and `startup.txt`
- [ ] Review logs for specific errors
- [ ] Verify file names and paths

### Environment Variable Issues
- [ ] Confirm all required settings are configured
- [ ] Check Azure Portal application settings
- [ ] Restart app after adding new settings

### Port Configuration
- [ ] Don't hardcode port numbers
- [ ] Use `os.environ.get('PORT', 5000)` in code
- [ ] Let Azure assign the port automatically

## Emergency Contacts and Resources

- [ ] Azure Documentation: https://docs.microsoft.com/en-us/azure/app-service/
- [ ] Azure Support (if available with your plan)
- [ ] Azure Status Page: https://status.azure.com/

---

**Next Steps After Successful Deployment:**
1. Set up CI/CD pipeline
2. Implement comprehensive monitoring
3. Add health checks and alerts
4. Plan for backup and disaster recovery
5. Consider containerization for better isolation