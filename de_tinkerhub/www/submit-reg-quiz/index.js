frappe.ready(()=>{
    $(".btn-start-quiz").click((e) => {
        $("#start-banner").addClass("hide");
		$("#quiz-form").removeClass("hide");
	});
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

const quiz_summary = (e = undefined) => {
	const response = $('form').serializeArray()
	let questions = response.map(({ name }) => decodeURIComponent(name));
	questions = [...new Set(questions)];
	let quiz = []
	questions.forEach(q=>{
		let data = {'question':q}
		let i = 1;
		response.forEach((r)=>{
			if(decodeURIComponent(r.name) === q){
				data[`answer_${i++}`] = r.value
			}
		});
		quiz.push(data)
	});
	frappe.call({
		method: "de_tinkerhub.de_tinkerhub.doctype.event_registration.event_registration.save_response",
		args: {
			event: $("#quiz-title").data("event"),
			result: quiz,
		},
		callback: (r) => {
			console.log(r.message)
			if(r.message){
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