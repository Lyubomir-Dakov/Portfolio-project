function toggleVisibility(listId) {
    var list = document.getElementById(listId);
    if (list.classList.contains("visible")) {
        list.classList.remove("visible");
    } else {
        list.classList.add("visible");
    }
}
