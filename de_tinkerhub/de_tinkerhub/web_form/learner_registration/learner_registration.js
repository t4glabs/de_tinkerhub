// frappe.ready(()=> {
// 	const a = frappe.session.user;
// 	const url = window.location.pathname;
// 	const main = document.querySelector('.page_content');

// 	if (a != 'Administrator'){
// 		if (url.endsWith('edit')) {
// 			const user = url.split('/')[2];	
// 			if (a !== user) {
// 				main.innerHTML = show_error;
// 			}
// 		} else if (!(url.endsWith(a) || url.endsWith(`${a}/`))) {
// 			main.innerHTML = show_error;
// 		}
// 	}
	
// })

// frappe.web_form.after_load = () => {
// 	if (window.location.pathname.endsWith("/new") && frappe.session.user) {
// 		let current_path = window.location.href;
// 		window.location.href = current_path.replace("/new", "/" + frappe.session.user);
// 	}
// }