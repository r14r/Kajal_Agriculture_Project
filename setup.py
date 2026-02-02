#!/usr/bin/env python
"""
Quick setup script for Django backend
"""

import os
import sys
import subprocess
import platform


def run_command(cmd, description):
    """Run a shell command"""
    print(f"\n{'='*60}")
    print(f"▶ {description}")
    print(f"{'='*60}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✓ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} - Failed")
        print(f"Error: {e}")
        return False


def main():
    """Main setup routine"""
    print("\n" + "="*60)
    print("Django Agriculture System - Quick Setup")
    print("="*60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8+ required")
        sys.exit(1)
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Detect OS
    current_os = platform.system()
    print(f"✓ OS: {current_os}")
    
    # Virtual environment setup
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        print(f"\n▶ Creating virtual environment...")
        if current_os == "Windows":
            run_command(f"python -m venv {venv_dir}", "Create virtual environment")
            activate_cmd = f"{venv_dir}\\Scripts\\activate && "
        else:
            run_command(f"python3 -m venv {venv_dir}", "Create virtual environment")
            activate_cmd = f"source {venv_dir}/bin/activate && "
    else:
        print(f"✓ Virtual environment already exists")
        if current_os == "Windows":
            activate_cmd = f"{venv_dir}\\Scripts\\activate && "
        else:
            activate_cmd = f"source {venv_dir}/bin/activate && "
    
    # Install dependencies
    if current_os == "Windows":
        install_cmd = f"{venv_dir}\\Scripts\\pip install -r requirements.txt"
    else:
        install_cmd = f"{activate_cmd}pip install -r requirements.txt"
    
    run_command(install_cmd, "Install dependencies")
    
    # Run migrations
    if current_os == "Windows":
        migrate_cmd = f"{venv_dir}\\Scripts\\python manage.py migrate"
    else:
        migrate_cmd = f"{activate_cmd}python manage.py migrate"
    
    run_command(migrate_cmd, "Run database migrations")
    
    # Print instructions
    print("\n" + "="*60)
    print("Setup Complete! 🎉")
    print("="*60)
    print("\nNext steps:")
    print("\n1. Create an admin user:")
    if current_os == "Windows":
        print(f"   {venv_dir}\\Scripts\\python manage.py createsuperuser")
    else:
        print(f"   {activate_cmd}python manage.py createsuperuser")
    
    print("\n2. Run the development server:")
    if current_os == "Windows":
        print(f"   {venv_dir}\\Scripts\\python manage.py runserver")
    else:
        print(f"   {activate_cmd}python manage.py runserver")
    
    print("\n3. Access the application:")
    print("   - Main API: http://localhost:8000/")
    print("   - Admin Panel: http://localhost:8000/admin/")
    print("   - Dashboard: http://localhost:8000/admin/")
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
