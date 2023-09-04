// Copyright (c) 2023, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on('Learner', {
    after_save: function(frm){
        // frappe.call({
        //     method: 'de_tinkerhub.de_tinkerhub.doctype.learner.learner.skill_filter',
        //     args: {
                
        //     },
        //     callback: r => {
        //         console.log('success')
        //     }
        // })
        frm.call('skill_filter')
            .then(r => {
                console.log('success')
            })
    }

});
