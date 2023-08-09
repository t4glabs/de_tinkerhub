frappe.ready(()=>{
    // $(".btn-start-quiz").click((e) => {
    //     $("#start-banner").addClass("hide");
	// 	$("#quiz-form").removeClass("hide");
	// });
    $(".option").click((e) => {
		if (!$("#check").hasClass("hide")) enable_check(e);
	});
	$("#summary").click((e) => {
		e.preventDefault();
		// if (!this.show_answers) check_answer();
		setTimeout(() => {
			quiz_summary(e);
		}, 500);
	});
});
const urlParams = new URLSearchParams(window.location.search);
const event_name = urlParams.get('event');
const quiz_summary = (e = undefined) => {
	const response = $('form').serializeArray()
	console.log('response: ', response)
	let questions = response.map(({ name }) => decodeURIComponent(name));
	questions = [...new Set(questions)];
	let quiz = []
	details = []
	questions.forEach(q=>{
		let data = {'question':q}
		let i = 1;
		data[`answer_1`] = ''
		response.forEach((r)=>{
			// if(decodeURIComponent(r.name) === q){
			// 	data[`answer_${i++}`] = decodeURIComponent(r.value)
			// }
			if(decodeURIComponent(r.name) === q){
				data[`answer_1`] += decodeURIComponent(r.value) + '<br>'
			
			}
		});
		quiz.push(data)
	});
	console.log('quiz: ', quiz)
	details[0] = document.getElementById('user-name').value;
	details[1] = document.getElementById('user-email').value;
	details[2]= document.getElementById('user-phone').value;
	// details.full_name = document.getElementById('user-name').value;
	// details.email = document.getElementById('user-email').value;
	// details.mobile = document.getElementById('user-phone').value;
	frappe.call({
		method: "de_tinkerhub.de_tinkerhub.doctype.event_registration.event_registration.save_response",
		args: {
			// event: $("#quiz-title").data("event"), 
			event: event_name,
			primary: details,
			result: quiz,
		},
		callback: (r) => {
			console.log(r.message)
			if(r.message){
				$(".user-info").addClass("hide");
				$("#quiz-form").addClass("hide");
				$("#submission-banner").removeClass("hide");
			}
			// $(".question").addClass("hide");
			// $("#summary").addClass("hide");
			// $(".quiz-footer span").addClass("hide");
			// $("#quiz-form").prepend(
			// 	`<div class="summary bold-heading text-center">
			// 		${__("Your score is")} ${data.message.score}
			// 		${__("out of")} ${total_questions}
			// 	</div>`
			// );
			// $("#try-again").attr("data-submission", data.message.submission);
			// $("#try-again").removeClass("hide");
			// self.quiz_submitted = true;
		},
	});
};