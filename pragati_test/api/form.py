import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def submit_form(data):
    if data is None:
        frappe.throw(_("No data provided."))

    if isinstance(data, str):
        data = frappe.parse_json(data)

    print("Parsed Data:", data)  # Debugging line
    data_dict = frappe._dict(data)

    # Check for existing entry
    existing_doc = frappe.db.exists('storage_list', {'advice_number': data_dict.advice_no, 'line_number': data_dict.line})
    if existing_doc:
        frappe.throw(_("An entry with Advice Number {} and Line Number {} already exists.").format(data_dict.advice_no, data_dict.line))

    # Create a new storage_list document
    doc = frappe.get_doc({
        'doctype': 'storage_list',
        'advice_number': data_dict.get('advice_no'),
        'line_number': data_dict.get('line'),
        'item': data_dict.get('item'),
        'description': data_dict.get('description'),
        'warehouse': data_dict.get('warehouse'),
        'from_location': data_dict.get('from_location'),
        'to_location': data_dict.get('to_location'),
        'storage_unit': data_dict.get('storage_unit')
    })
    
    # Insert the document into the database
    doc.insert()
    frappe.db.commit()
    
    return {"message": _("Data submitted successfully"), "status": "success"}
