# Add Waydroid scripts
curl -L https://raw.githubusercontent.com/clearfraction/bundles/master/cf-waydroid-preinstall.sh -o /tmp/waydroid/usr/bin/cf-waydroid-preinstall.sh
curl -L https://raw.githubusercontent.com/clearfraction/bundles/master/cf-waydroid-init.sh -o /tmp/waydroid/usr/bin/cf-waydroid-init.sh
curl -L https://raw.githubusercontent.com/clearfraction/bundles/master/cf-waydroid-uninstall.sh -o /tmp/waydroid/usr/bin/cf-waydroid-uninstall.sh
chmod +x /tmp/waydroid/usr/bin/{cf-waydroid-preinstall.sh,cf-waydroid-init.sh,cf-waydroid-uninstall.sh}

