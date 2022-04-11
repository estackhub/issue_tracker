frappe.ui.form.on("Issue", {
    refresh(frm){
		//console.table(frm.doc);
		if (frm.doc.docstatus === 0 && !frm.is_new()) {
			frm.trigger("show_progress_for_Issues");
		}
	},

    show_progress_for_Issues: function(frm) {
		/**Standard Task Status 
		 * Open
		 * Working
		 * Pending Review
		 * Overdue
		 * Template
		 * Completed
		 * Cancelled
		*/
		//css_list: 1:primary,2:warning,3:danger,4:success| unknow: info,secondary,dark & light
		
		let bars = [];
		let message = '';
		let title = '';

		let progress_class = [
			{tstatus:"Open",tstep:1, tclass:"progress-bar-danger"},
			{tstatus:"Working",tstep:2,tclass:"progress-bar-warning"},
			{tstatus:"Pending Review",tstep:3,tclass:"progress-bar-info"} ,
			{tstatus:"Review",tstep:4,tclass:"progress-bar-primary"},
			{tstatus:"Completed",tstep:5,tclass:"progress-bar-success"}
		];

		frappe.call({
			method:"issue_tracker_bar.issue_tracker_bar.app.tracker_bar.get_all_task",
			args:{issue:frm.doc.name},
			callback: function (r) {
				let m_tasks = r.message;
				m_tasks.forEach(t => {
					title = __("Task- {0}, title- <i>{1}</i>, progress status is : {2}", [t.name,t.subject ,t.status.bold()]);
					let tsc = progress_class.find(function(p, i){
						if(p.tstatus == t.status)
						return true;
					});
					bars =[{
						'title': title,
						'width': tsc.tstep / progress_class.length * 100  + '%',
						'progress_class': tsc.tclass
					}];
					message = title;
					frm.dashboard.add_progress(__('Status'), bars, message);
					
				} )
			}
		});			
		
	},
});