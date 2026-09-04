#!/usr/bin/env python3
"""
Azure Deployment Script for Mix Integrate API
This script helps automate the deployment process to Azure Web App
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# Windows consoles default to cp1252 and choke on the emoji below.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def run_command(command, check=True):
    """Run a shell command and return the result"""
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        if result.stdout:
            print(f"Output: {result.stdout}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return None

def check_azure_cli():
    """Check if Azure CLI is installed"""
    result = run_command("az --version", check=False)
    return result is not None and result.returncode == 0

def check_azure_login():
    """Check if user is logged in to Azure"""
    result = run_command("az account show", check=False)
    return result is not None and result.returncode == 0

def create_requirements_file():
    """Create or verify requirements.txt exists"""
    if not Path("requirements.txt").exists():
        print("Creating requirements.txt...")
        # Minimal requirements for Azure deployment
        requirements = [
            "Flask==3.1.0",
            "gunicorn==23.0.0",
            "requests==2.32.3",
            "Werkzeug==3.1.3"
        ]
        with open("requirements.txt", "w") as f:
            f.write("\n".join(requirements))
        print("✅ requirements.txt created")
    else:
        print("✅ requirements.txt already exists")

def create_procfile():
    """Create or verify Procfile exists"""
    if not Path("Procfile").exists():
        print("Creating Procfile...")
        with open("Procfile", "w") as f:
            f.write("web: gunicorn app:app")
        print("✅ Procfile created")
    else:
        print("✅ Procfile already exists")

def create_startup_file():
    """Create or verify startup.txt exists"""
    if not Path("startup.txt").exists():
        print("Creating startup.txt...")
        with open("startup.txt", "w") as f:
            f.write("gunicorn --bind=0.0.0.0 --timeout 600 app:app")
        print("✅ startup.txt created")
    else:
        print("✅ startup.txt already exists")

def check_deployment_files():
    """Check if all required deployment files exist"""
    required_files = [
        "app.py",
        "requirements.txt",
        "Procfile",
        "startup.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    else:
        print("✅ All required deployment files exist")
        return True

def validate_environment_variables():
    """Check if required environment variables are set"""
    required_vars = [
        "MIX_CLIENT_ID",
        "MIX_CLIENT_SECRET",
        "MIX_USERNAME",
        "MIX_PASSWORD"
    ]
    
    print("Checking required environment variables for Azure App Settings:")
    for var in required_vars:
        value = os.environ.get(var)
        if value:
            print(f"✅ {var} is set")
        else:
            print(f"⚠️  {var} is not set (will need to configure in Azure Portal)")
    
    print("\n📋 Azure App Settings to configure:")
    print("- MIX_CLIENT_ID = <your-client-id>")
    print("- MIX_CLIENT_SECRET = <your-client-secret>") 
    print("- MIX_USERNAME = <your-username>")
    print("- MIX_PASSWORD = <your-password>")

def show_next_steps():
    """Display next steps for manual deployment"""
    print("\n" + "="*60)
    print("🚀 NEXT STEPS FOR AZURE DEPLOYMENT")
    print("="*60)
    
    print("\n1. VSCode Deployment Method:")
    print("   • Install Azure extensions in VSCode")
    print("   • Login to Azure (Ctrl+Shift+P → 'Azure: Sign In')")
    print("   • Right-click project folder → 'Deploy to Web App...'")
    print("   • Follow the prompts to create App Service")
    
    print("\n2. Azure Portal Method:")
    print("   • Go to https://portal.azure.com")
    print("   • Create new Web App")
    print("   • Choose Python 3.12 runtime")
    print("   • Configure environment variables in App Settings")
    
    print("\n3. Required Environment Variables (configure in Azure):")
    print("   • MIX_CLIENT_ID = <your-client-id>")
    print("   • MIX_CLIENT_SECRET = <your-client-secret>")
    print("   • MIX_USERNAME = <your-username>")
    print("   • MIX_PASSWORD = <your-password>")
    
    print("\n4. Post-Deployment Testing:")
    print(f"   • Visit: https://your-app-name.azurewebsites.net/health")
    print(f"   • Test: https://your-app-name.azurewebsites.net/organisations")
    
    print("\n📚 For detailed instructions, see:")
    print("   • azure_deployment_guide.md")
    print("   • azure_deployment_checklist.md")

def main():
    """Main deployment preparation function"""
    print("🚀 Azure Deployment Preparation for Mix Integrate API")
    print("="*60)
    
    # Check if we're in the right directory
    if not Path("app.py").exists() and not Path("app.py").exists():
        print("❌ Please run this script from your project directory")
        sys.exit(1)
    
    print("\n📁 Checking deployment files...")
    create_requirements_file()
    create_procfile()
    create_startup_file()
    
    if not check_deployment_files():
        sys.exit(1)
    
    print("\n🔍 Azure CLI Status:")
    if check_azure_cli():
        print("✅ Azure CLI is installed")
        if check_azure_login():
            print("✅ You are logged in to Azure")
        else:
            print("⚠️  You need to login: Run 'az login'")
    else:
        print("⚠️  Azure CLI not installed (install from: https://aka.ms/installazurecliwindows)")
    
    print("\n🔐 Environment Variables:")
    validate_environment_variables()
    
    print("\n✅ Pre-deployment checks complete!")
    show_next_steps()

if __name__ == "__main__":
    main()