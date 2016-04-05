function refreshTracker () {
    var assignment = parseInt($("#assignment").val())
    $.get("http://localhost:5000/assignment/" + assignment).done(function (result) {
        $("#tracker tbody").html("")
        result.data.forEach(function (row) {
            var tr = $("<tr>")
            tr.append($("<td>").text(row.name))
            tr.append($("<td>").text(row.max_tests_passed))
            tr.append($("<td>").text(row.tests_failed))
            $("#tracker tbody").append(tr)
        })
    })
}
refreshTracker()
setInterval(refreshTracker, 3000)
