# 🚀 Azure Deployment Guide - Mix Integrate API

This repository contains everything you need to deploy your Flask application to Azure Web App through Visual Studio Code.

## 📋 Quick Start

1. **Review the comprehensive guide**: [`azure_deployment_guide.md`](./azure_deployment_guide.md)
2. **Follow the checklist**: [`azure_deployment_checklist.md`](./azure_deployment_checklist.md)
3. **Run the deployment script**: `python deploy_to_azure.py`

## 📁 Files Created for Deployment

| File | Purpose | Action Required |
|------|---------|----------------|
| `azure_deployment_guide.md` | Complete step-by-step deployment guide | Read and follow |
| `azure_deployment_checklist.md` | Interactive checklist for deployment | Check off items as you complete |
| `deploy_to_azure.py` | Automated pre-deployment validation | Run before deployment |
| `startup.txt` | Azure App Service startup configuration | ✅ Ready to use |
| `app.py` | Production entrypoint (env-var credentials, /health) | Deployed as-is |

## ⚡ Quick Deployment (5 Minutes)

### Prerequisites
- [ ] VSCode with Azure extensions installed
- [ ] Azure subscription
- [ ] Project files ready

### Steps

1. **Setup Azure App Service**
   - VSCode: Right-click Azure Explorer → "Create New Web App"
   - Choose Python 3.12 runtime
   - Select Free tier (F1) for testing

2. **Configure Environment Variables**
   - Go to Azure Portal → Your App Service → Configuration
   - Add these Application Settings:
     ```
     MIX_CLIENT_ID = <your-client-id>
     MIX_CLIENT_SECRET = <your-client-secret>
     MIX_USERNAME = <your-username>
     MIX_PASSWORD = <your-password>
     ```

3. **Deploy**
   - Right-click your project folder in VSCode
   - Select "Deploy to Web App..."
   - Choose your created App Service
   - Wait for deployment to complete

4. **Test**
   - Visit: `https://your-app-name.azurewebsites.net/health`
   - Should return: `{"status": "healthy", "app": "Mix Integrate API"}`

## 🔧 Important Notes

### Security
- **⚠️ CRITICAL**: Your current `app.py` has hardcoded credentials
- **✅ SOLUTION**: `app.py` now reads credentials from environment variables
- **✅ SECURITY**: Configure credentials in Azure App Settings (not in code)

### Application Structure
- **Main App**: `app.py`
- **Web Server**: `gunicorn` (configured in Procfile)
- **Dependencies**: All packages in `requirements.txt`
- **Startup**: Configured in `startup.txt`

### Azure Configuration
- **Runtime**: Python 3.12
- **Port**: Automatically assigned by Azure
- **Health Check**: `/health` endpoint available
- **All API Endpoints**: Available after deployment

## 📊 Your API Endpoints

After deployment, your API will be available at `https://your-app-name.azurewebsites.net`:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Health check |
| `/organisations` | GET | Get organizations |
| `/sites` | GET | Get sites for organizations |
| `/assets` | GET | Get assets for organizations |
| `/drivers` | GET | Get drivers for organizations |
| `/events` | GET | Get events for organizations |
| `/positions` | POST | Get positions |
| `/trips` | POST | Get trips by date range |
| `/positions_date_range` | POST | Get positions by date range |
| `/events_since` | POST | Get events since timestamp |
| `/events_since_filtered` | POST | Get filtered events |
| `/positions_since` | POST | Get positions since timestamp |
| `/trips_since` | POST | Get trips since timestamp |

## 🎯 Expected Results

After successful deployment:

✅ **Azure App Service**: Running and healthy  
✅ **Health Check**: `/health` returns `{"status": "healthy"}`  
✅ **API Endpoints**: All endpoints accessible and functional  
✅ **Security**: Credentials stored in Azure App Settings  
✅ **Monitoring**: Logs accessible through Azure Portal  

## 🔍 Troubleshooting

### Common Issues

1. **Deployment Fails**
   - Check all files are present (`app.py`, `startup.txt`, etc.)
   - Verify Python 3.12 runtime selected
   - Check Azure logs for specific errors

2. **API Returns Errors**
   - Verify environment variables are set correctly
   - Check Azure App Settings configuration
   - Review logs in Azure Portal

3. **Health Check Fails**
   - Ensure the latest `app.py` is deployed
   - Check startup configuration
   - Review application logs

### Getting Help

- **Azure Logs**: Azure Portal → App Service → Log Stream
- **VSCode Logs**: Right-click App Service → View Logs
- **Health Check**: Always test `/health` endpoint first

## 💰 Cost Considerations

- **Free Tier**: Suitable for testing (F1 plan)
- **Production**: Consider Standard tier for better performance
- **Monitoring**: Watch usage in Azure Portal billing

## 🚀 Next Steps

After successful deployment:

1. **Monitor**: Set up Application Insights
2. **Secure**: Add authentication/authorization
3. **Scale**: Configure auto-scaling if needed
4. **Backup**: Set up backup strategies
5. **CI/CD**: Implement continuous deployment

## 📚 Additional Resources

- [Complete Deployment Guide](./azure_deployment_guide.md)
- [Deployment Checklist](./azure_deployment_checklist.md)
- [Azure App Service Documentation](https://docs.microsoft.com/en-us/azure/app-service/)
- [VSCode Azure Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-azureappservice)

---

**🎉 Ready to deploy? Start with the [deployment guide](./azure_deployment_guide.md)!**