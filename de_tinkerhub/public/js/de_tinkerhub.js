let show_form = () => {

    let fields = registration_fields()
    let question_dialog = new frappe.ui.Dialog({
        title: "Event Registration",
        fields: fields,
        primary_action: data => {
            event_registration(data)
            console.log(data)
            question_dialog.hide()
        }
    });

    question_dialog.show();
};


event_registration = (data) => {
    let url = window.location.href,
        last = url.split('/')[4]

    frappe.call({
    method: 'de_tinkerhub.services.rest.event_registration',
    args: {
        'event': last,
        'email' : data.email,
        'full_name': data.full_name,
        'mobile_no': data.contact
    },
    callback: r => {

    }
})
}

const registration_fields = () => {
    let full_name, email
    if(frappe.session.user != "Guest"){
        full_name = frappe.full_name
        email = frappe.session.user
    }

	let dialog_fields = [
        {
            label: 'Full Name',
            fieldname: 'full_name',
            fieldtype: 'Data',
            reqd: 1,
            default: full_name || ""
        },
        {
            label: 'Email',
            fieldname: 'email',
            fieldtype: 'Data',
            reqd: 1,
            default: email || ""
        },
        {
            label: 'Contact Number',
            fieldname: 'contact',
            fieldtype: 'Data',
            reqd: 1
        }
    ]

    if (full_name && email) {
        dialog_fields[0].read_only = 1
        dialog_fields[1].read_only = 1
    }

	return dialog_fields;
};

