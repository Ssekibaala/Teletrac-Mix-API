# Azure Web App Deployment Guide for Flask Application

## Prerequisites

1. **Azure Account**: You'll need an active Azure subscription
2. **Visual Studio Code** with Azure Extensions installed
3. **Python 3.12** (matching your .python-version file)
4. **Git** (for version control)

## Step 1: Install Required VSCode Extensions

1. Install the following VSCode extensions:
   - **Azure Account** extension
   - **Azure App Service** extension
   - **Azure Resources** extension (optional)

## Step 2: Prepare Your Application

Your application is already well-prepared with:
- ✅ `Procfile` with `web: gunicorn app:app`
- ✅ `requirements.txt` with all dependencies
- ✅ Flask application structure

### Additional Configuration Needed

Create a `startup.txt` file for Azure:

```
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

## Step 3: Create Azure App Service

### Method 1: Using VSCode (Recommended)

1. **Login to Azure**:
   - Open VSCode Command Palette (Ctrl+Shift+P)
   - Run "Azure: Sign In"
   - Follow the authentication process

2. **Create App Service**:
   - In Azure Explorer, right-click "App Service"
   - Select "Create New Web App"
   - Choose your subscription
   - Enter a globally unique name (e.g., `mix-integrate-api`)
   - Select region (choose closest to your users)
   - Select runtime stack: **Python 3.12**
   - Choose pricing tier (Free tier available)

### Method 2: Using Azure Portal

1. Go to [Azure Portal](https://portal.azure.com)
2. Create a new resource
3. Search for "Web App"
4. Configure:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Create new or use existing
   - **Name**: Unique app name
   - **Runtime**: Python 3.12
   - **Region**: Choose appropriate region
   - **App Service Plan**: Free tier (F1) for development

## Step 4: Configure Application Settings

### In Azure Portal:

1. Go to your App Service
2. Navigate to **Configuration**
3. Add these application settings:

```
FLASK_APP = app.py
FLASK_ENV = production
PYTHONPATH = /home/site/wwwroot
```

4. **Save** and **Restart** the app

### Security Considerations:

⚠️ **IMPORTANT**: Your current code contains hardcoded credentials. You need to move these to Azure Application Settings:

1. Go to **Configuration** in your App Service
2. Add these settings:
   - `MIX_CLIENT_ID` = `<your-client-id>`
   - `MIX_CLIENT_SECRET` = `<your-client-secret>`
   - `MIX_USERNAME` = `<your-username>`
   - `MIX_PASSWORD` = `<your-password>`

3. **Remove** these from your code (update `app.py`)

## Step 5: Update Your Code for Azure

Create a production-ready version of your app:

### Update app.py for production:

```python
import os
from flask import Flask, jsonify, request
import requests
import time
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get credentials from environment variables
MIX_CLIENT_ID = os.environ.get('CLIENT_ID', '<your-client-id>')
MIX_CLIENT_SECRET = os.environ.get('CLIENT_SECRET', '<your-client-secret>')
MIX_USERNAME = os.environ.get('USERNAME', '<your-username>')
MIX_PASSWORD = os.environ.get('PASSWORD', '<your-password>')
SCOPE = 'offline_access MiX.Integrate'
TOKEN_URL = 'https://identity.za.mixtelematics.com/core/connect/token'

# Rest of your code remains the same...
```

## Step 6: Deploy Using VSCode

### Option A: Deploy using Azure Extension

1. **Right-click** on your project folder
2. Select **"Deploy to Web App..."**
3. Choose your created App Service
4. Confirm deployment

### Option B: Using Command Line

1. Install Azure CLI:
   ```bash
   # Windows (using winget)
   winget install Microsoft.AzureCLI
   
   # Or download from: https://aka.ms/installazurecliwindows
   ```

2. Login and deploy:
   ```bash
   # Login to Azure
   az login
   
   # Deploy
   az webapp deploy --resource-group YourResourceGroup --name YourAppName --src-path . --type zip
   ```

## Step 7: Verify Deployment

1. **Check deployment status** in Azure Portal
2. **Visit your app**: `https://your-app-name.azurewebsites.net`
3. **Test endpoints**:
   - `https://your-app-name.azurewebsites.net/organisations`
   - `https://your-app-name.azurewebsites.net/sites?organisationIds=123,456`

## Step 8: Configure Custom Domain (Optional)

1. In Azure Portal, go to **Custom domains**
2. Add your custom domain
3. Update DNS records as instructed

## Monitoring and Logs

### Accessing Logs:

1. **In Azure Portal**: Go to **App Service** → **Log stream**
2. **In VSCode**: Right-click App Service → **View Logs**

### Application Insights (Recommended):

1. Enable Application Insights during app creation
2. Monitor performance, errors, and usage
3. Set up alerts for issues

## Troubleshooting Common Issues

### 1. Import Errors
- Ensure all dependencies are in `requirements.txt`
- Check Python version compatibility

### 2. Startup Failures
- Verify `Procfile` or `startup.txt` is correct
- Check logs for specific error messages

### 3. Environment Variables
- Ensure all required settings are configured
- Use Azure Portal to verify environment variables

### 4. Port Issues
- Azure assigns a port automatically
- Don't hardcode port numbers in your code

## Cost Optimization

- Use **Free Tier** (F1) for development/testing
- Consider **Consumption Plan** for better performance
- Monitor usage in Azure Portal

## Security Best Practices

1. **Never commit credentials** to version control
2. **Use Azure Key Vault** for sensitive data
3. **Enable HTTPS** (enabled by default)
4. **Use Managed Identity** when possible
5. **Implement authentication** for production use

## Next Steps

1. Set up **CI/CD pipeline** with GitHub Actions
2. Implement **health checks**
3. Add **monitoring and alerting**
4. Set up **backup strategies**
5. Consider **container deployment** for better isolation

## Useful Commands

```bash
# Check deployment logs
az webapp log tail --resource-group MyResourceGroup --name MyApp

# Restart app
az webapp restart --resource-group MyResourceGroup --name MyApp

# Scale up/down
az webapp scale plan --resource-group MyResourceGroup --name MyApp --plan F1
```

Your Flask application is well-structured and ready for Azure deployment!