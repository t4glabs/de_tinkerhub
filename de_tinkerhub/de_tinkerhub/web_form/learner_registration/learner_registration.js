frappe.ready(function() {

	let a = frappe.session.user
	if (!(window.location.pathname.endsWith(a) || window.location.pathname.endsWith(`${a}/`))) {
		let show_error = `
			<style>
			.page-card {
				max-width: 360px;
				padding: 15px;
				margin: 70px auto;
				border-radius: 4px;
				background-color: var(--fg-color);
				box-shadow: var(--shadow-base);
			}
			
			.page-card .page-card-head {
				padding: 10px 15px;
				margin: -15px;
				margin-bottom: 15px;
				border-bottom: 1px solid var(--border-color);
			}
			
			.page-card-head h4 {
				font-size: 18px;
				font-weight: 600;
			}
			
			.page-card .page-card-head .indicator {
				color: #36414C;
				font-size: 14px;
			}
			
			.page-card .page-card-head .indicator::before {
				margin: 0 6px 0.5px 0px;
			}
			
			.page-card {
				border: 0;
				max-width: 450px;
				margin: auto;
				border-radius: var(--border-radius-md);
				padding: 40px 60px;
			}
			</style>
			<div class="page-card">
				<h5 class="page-card-head">
					<span class="indicator red">
						Not Permitted</span>
				</h5>
				<div class="page-card-body">
			
					<p>You don't have the permissions to access this document</p>
					
					<div><a href="/login?redirect-to=/update-profile/learner01@gmail.com/" class="btn btn-primary btn-sm">
						Login</a></div>
				
			
				</div>
			</div>
			`
		let main = document.querySelector('.page_content')
		main.innerHTML = show_error
		
	}
})

// frappe.web_form.after_load = () => {
// 	if (window.location.pathname.endsWith("/new") && frappe.session.user) {
// 		let current_path = window.location.href;
// 		window.location.href = current_path.replace("/new", "/" + frappe.session.user);
// 	}
// }