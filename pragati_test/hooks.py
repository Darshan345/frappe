# /home/darshan/frappe/apps/pragati_test/hooks.py


app_name = "pragati_test"
app_title = "Pragati"
app_publisher = "Pragati"
app_description = "Info about stores and others"
app_email = "pragati@automation.in"
app_license = "MIT"

# Whitelisted methods for API access
override_whitelisted_methods = {
    "pragati_test.api.form.submit_form": "pragati_test.api.form.submit_form"
}

# Include CSS files in the app and web templates
app_include_css = "/assets/pragati_test/css/custom_style.css"  # Path to your CSS file
web_include_css = "/assets/pragati_test/css/custom_style.css"   # Include in web templates

# Include JavaScript files in the app and web templates
app_include_js = ["/assets/pragati_test/js/website_script.js"]  # Ensure this path is correct
web_include_js = ["/assets/pragati_test/js/website_script.js"]   # Include in web templates if necessary

# Content Security Policy
csp = {
    "default-src": "'self' http://127.0.0.1:3001",  # Allow self and your specific server
    "img-src": "'self' data:",
    "script-src": "'self' 'unsafe-inline' 'unsafe-eval'",
    "style-src": "'self' 'unsafe-inline'",  # Allow inline styles
}

# Optional: If your web server isn't setting CSP headers, you can add a header override
override_csp = {
    "Content-Security-Policy": "default-src 'self' http://127.0.0.1:3001; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:; style-src 'self' 'unsafe-inline';"
}

# Add CORS headers
def before_request():
    import frappe
    frappe.local.response.headers["Access-Control-Allow-Origin"] = "*"
    frappe.local.response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    frappe.local.response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Frappe-API-Key, X-Frappe-API-Secret"
