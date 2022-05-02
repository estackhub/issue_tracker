frappe.ui.form.on("Issue", {
    refresh(frm){
		if (frm.doc.docstatus === 0 && !frm.is_new()) {
			frm.trigger("show_progress_for_Issues");
		}
		
	},

    show_progress_for_Issues: function(frm) {
		let bars = [];
		let message = '';
		let title = '';
		let nwstyle = ";background-color:";
		var status_list=[] ;

		/*api call: .replace(/;+$/,"")*/
		frappe.call({
			method:"issue_tracker_bar.issue_tracker_bar.app.tracker_bar.get_all_task",
			args:{issue:frm.doc.name},
			callback: function (r) {
				if (r.message.length > 0) {
					//console.log(r.message);
					let m_tasks = r.message;
					
					m_tasks.forEach(t => {
						title = __("<i class='indicator-pill whitespace-nowrap {2}'>{0}</i>: \
						<span style='padding-right:10px'>{1} </span>", [t.subject ,t.status.bold(),t.tcolor]);
						
						bars.push({
							'title': title,
							'width': 1 / m_tasks.length * 100  + '%'+nwstyle+t.tcolor+';',
							'progress_class': ''
						});
						message += title;						
						
					})
					frm.dashboard.add_progress(__('Status'), bars, message);
				
				}
				
			}
		});
		
	},
});

/***
 <a class="badge-wrapper bullet" href="/c/erpnext/support">
	<span class="badge-category-bg" style="background-color: #0088CC;"></span>
	<span data-drop-close="true" class="badge-category clear-badge" title="">
	<span class="category-name">Support</span>
	</span>
</a>
 */