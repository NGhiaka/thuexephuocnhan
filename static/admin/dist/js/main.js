 $(document).ready(function() {
    $('body').removeClass('preloading');
    $('#preload').hide();
    $('.select2').select2();

    $('#mydatatable').DataTable();
    // $('.filterable .btn-filter').click(function(){
    //     var $panel = $(this).parents('.filterable'),
    //     $filters = $panel.find('.filters input'),
    //     $tbody = $panel.find('.table tbody');
    //     if ($filters.prop('disabled') == true) {
    //         $filters.prop('disabled', false);
    //         $filters.first().focus();
    //     } else {
    //         $filters.val('').prop('disabled', true);
    //         $tbody.find('.no-result').remove();
    //         $tbody.find('tr').show();
    //     }
    // });

    // $('.filterable .filters input').keyup(function(e){
    //     /* Ignore tab key */
    //     var code = e.keyCode || e.which;
    //     if (code == '9') return;
    //     /* Useful DOM data and selectors */
    //     var $input = $(this),
    //     inputContent = $input.val().toLowerCase(),
    //     $panel = $input.parents('.filterable'),
    //     column = $panel.find('.filters th').index($input.parents('th')),
    //     $table = $panel.find('.table'),
    //     $rows = $table.find('tbody tr');
    //     /* Dirtiest filter function ever ;) */
    //     var $filteredRows = $rows.filter(function(){
    //         var value = $(this).find('td').eq(column).text().toLowerCase();
    //         return value.indexOf(inputContent) === -1;
    //     });
    //     /* Clean previous no-result if exist */
    //     $table.find('tbody .no-result').remove();
    //     /* Show all rows, hide filtered ones (never do that outside of a demo ! xD) */
    //     $rows.show();
    //     $filteredRows.hide();
    //     /* Prepend no-result row if all rows are filtered */
    //     if ($filteredRows.length === $rows.length) {
    //         $table.find('tbody').prepend($('<tr class="no-result text-center"><td colspan="'+ $table.find('.filters th').length +'">No result found</td></tr>'));
    //     }
    // });

    ////===========filter==============
    $("#my-search-text").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
    
    $.datepicker.regional["vi-VN"] =
        {
            closeText: "Đóng",
            prevText: "Trước",
            nextText: "Sau",
            currentText: "Hôm nay",
            monthNames: ["Tháng một", "Tháng hai", "Tháng ba", "Tháng tư", "Tháng năm", "Tháng sáu", "Tháng bảy", "Tháng tám", "Tháng chín", "Tháng mười", "Tháng mười một", "Tháng mười hai"],
            monthNamesShort: ["Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín", "Mười", "Mười một", "Mười hai"],
            dayNames: ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"],
            dayNamesShort: ["CN", "Hai", "Ba", "Tư", "Năm", "Sáu", "Bảy"],
            dayNamesMin: ["CN", "T2", "T3", "T4", "T5", "T6", "T7"],
            weekHeader: "Tuần",
            dateFormat: "dd/mm/yy",
            firstDay: 1,
            isRTL: false,
            showMonthAfterYear: false,
            yearSuffix: ""
    };
    $('#datepicker').datetimepicker({
        theme:'dark',
        timepicker:false,
        format:'Y-m-d',
        formatDate:'Y-m-d',
        
    });

    $('#datepicker1').datetimepicker({
        theme:'dark',
        yearOffset:0,
        language:'vn',
        timepicker:false,
        format:'Y-m-d',
        formatDate:'Y-m-d',
        startdate: new Date(),
        // defaultDate: new Date(),
        minDate:'0', // yesterday is minimum date
        onSelect: function(dateStr) 
        {      
            $("#datepicker2").val(dateStr);
            $("#datepicker2").datepicker("option",{ minDate: new Date(dateStr)});
        },
        // maxDate:'+1970/01/02' // and tommorow is maximum date calendar
    });
    $('#datepicker2').datetimepicker({
        theme:'dark',
        yearOffset:0,
        lang:'vn',
        timepicker:false,
        format:'Y-m-d',
        formatDate:'Y-m-d',
        
        // defaultDate: new Date(),
        // minDate:'0', // yesterday is minimum date
        // maxDate:'+1970/01/02' // and tommorow is maximum date calendar
    });
    $('#timepicker1').datetimepicker({
        theme:'dark',
        datepicker:false,
        format:'H:i',
        step:5
    });
    var eventData = [
        {"date":"2017-09-09","badge":true,"title":"Example 1"},
        {"date":"2017-09-09","badge":true,"title":"Example 2"}
    ]

    $("#my-calendar").zabuto_calendar({
        theme:'dark',
        // cell_border: true,
        today: true,
        lang: "vn",
        weekstartson: 0,
        data: eventData,
        nav_icon: {
            prev: '<i class="fa fa-chevron-circle-left"></i>',
            next: '<i class="fa fa-chevron-circle-right"></i>'
        },
    });

    // var data = [
    //     {
    //         "badge":   true,
    //         "classname":   "purple-event",
    //         "date":    "2017-07-06",
    //         "title":   "Tonight",
    //         "footer":  "At Paisley Park",
    //         "body":    "Nguyễn văn tèo",
    //     },
    //     {   
    //         "badge":   true,
    //         "classname":   "purple-event",
    //         "date":    "2017-07-30",
    //         "title":   "Tonight",
    //         "footer":  "At Paisley Park",
    //         "body":    "Nguyễn văn tí",
    //     },
    //     {   
    //         "badge":   true,
    //         "classname":   "purple-event",
    //         "date":    "2017-07-29",
    //         "title":   "Tonight",
    //         "footer":  "At Paisley Park",
    //         "body":    "Nguyễn văn tèo",
    //     }
    // ];

    // console.log("i'm clicked");
    
    // function load_data() {
    //     console.log("i'm clicked");
    //     $.ajax({
    //         type: "POST",
    //         url: "/admin/lichtrinh/json",
    //         contentType: "application/json; charset=utf-8",
    //         dataType: "json",
    //         cache: false,
    //         data: name
    //         success: function (data) {
    //             var list = $.parseJSON(data.d);
    //             console.log(data.name);
    //             // $("#test").zabuto_calendar({
    //             //     today: true,
    //             //     language: "vn",
    //             //     weekstartson: 0,
    //             //     nav_icon: {
    //             //         prev: '<i class="fa fa-chevron-circle-left"></i>',
    //             //         next: '<i class="fa fa-chevron-circle-right"></i>'
    //             //     },
    //             //     data: list,
    //             // });
                
    //         },
    //         error: function (data) {
    //             console.log(data.d);
    //         }
    //     });
    // };


    // load_data();


    // $("#test").zabuto_calendar({
    //     today: true,
    //     language: "vn",
    //     weekstartson: 0,
    //     nav_icon: {
    //         prev: '<i class="fa fa-chevron-circle-left"></i>',
    //         next: '<i class="fa fa-chevron-circle-right"></i>'
    //     },
    //     // ajax: {
    //     //    url: "/admin/schedule/json",
    //     //    modal: true
    //     // }
    //     data: load_data(),
        
    // });

    $('.dropdown-toggle').dropdown()

});

function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    console.log(newElement.find(':input'));
    newElement.find(':input').each(function() {
        if ($(this).attr('name')!=null){
            var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });

    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    console.log(selector);
    var conditionRow = $('.form-row:not(:last)');
    conditionRow.find('.btn.add-form-row')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row').addClass('remove-form-row')
    .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');
    return false;
}
function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row').remove();
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore('.form-row:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
});

$(document).on('change', '.choose-element', function(e){
    var value = $(this).val();
    var id = this.id;
    if(value){
        console.log(id);
        console.log(value);
        $("#new-" + id).hide();
    }else{
        console.log("sdasd");
        $("#new-" + id).show();
    }
});

function ImageDetail(path, id){
    var str = "<img src='"+ path + "' class='img-thumbnail img-responsive' >";
    str += '<div class="action-img">';
    str += "<a href='/admin/anh/xoa/"+ id+ "' class='btn btn-danger'><i class='fa fa-trash fa-lg' aria-hidden='true'></i> Xóa</a>";
    str += '</div>';
    $(".show-img").html(str);
}

// $(".caption-title").each(function(i){
//     var len=$(this).text().length;
//     if(len>200)
//     {
//       $(this).text($(this).text().substr(0,200)+'...');
//     }
// });

