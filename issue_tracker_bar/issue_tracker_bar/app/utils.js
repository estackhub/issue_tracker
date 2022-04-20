frappe.ui.form.on("Issue", {
    refresh(frm){
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
		let barlenght = 0;

		let progress_class = [
			{tstatus:"Open",tstep:1, tclass:"progress-bar-danger"},
			{tstatus:"Working",tstep:1,tclass:"progress-bar-warning"},
			{tstatus:"Pending",tstep:2,tclass:"progress-bar-primary"} ,
			{tstatus:"Review",tstep:3,tclass:"progress-bar-info"},
			{tstatus:"Completed",tstep:4,tclass:"progress-bar-success"}
		];

		frappe.call({
			method:"issue_tracker_bar.issue_tracker_bar.app.tracker_bar.get_all_task",
			args:{issue:frm.doc.name},
			callback: function (r) {
				if (r.message.length > 0) {
					let m_tasks = r.message;
					
					m_tasks.forEach(t => {
						title = __("[<i>{0}</i>]: {1}, <span style='padding-right:4px'></span>", [t.subject ,t.status.bold()]);
						let tsc = progress_class.find(function(p, i){
							if(p.tstatus == t.status)
							return true;
						});
						bars.push({
							'title': title,
							'width': 1 / m_tasks.length * 100  + '%',
							'progress_class': tsc.tclass
						});
						message += title;						
						
					})
					frm.dashboard.add_progress(__('Status'), bars, message);
				
				}
				
			}
		});			
		
	},
});
