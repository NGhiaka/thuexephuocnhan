$(document).ready(function() {
  // SCHEDUL
  var schedule = document.getElementById('schedule-calendar');
  var link = $(schedule).data('schedule-url');
  $.ajax({
    url: link,
    data: {},
    dataType: 'json',
    success: function (data) {
      var resData = JSON.parse(data);
      var fullCal = Calendar("#schedule-calendar", resData);
    }
  });
  // END
});

function Calendar(id, data){
  var fullCalendar = $(id).fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay,listWeek'
    },
    defaultDate: Date.now(),
    locale: 'vi',
    // themeSystem: themeSystem,
    navLinks: true, // can click day/week names to navigate views
    editable: true,
    eventLimit: true, // allow "more" link when too many events
    events: data,
  });
  return fullCalendar;
}

// GOOGLE MAP

// END GOOGLE MAP