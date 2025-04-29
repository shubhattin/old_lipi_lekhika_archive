let font_loaded = [];
$l("#font").on("change", function () {
    let v = this.value;
    $l(".t").css("font-family", `"${v}"`);
    if (v != "Calibri" && font_loaded.indexOf(v) == -1) {
        var font = new FontFace(v, `url("${v}.woff2")`);
        font.load().then(function (loaded_face) {
            document.fonts.add(loaded_face);
        })
        font_loaded.push(v);
    }
});
$l("#font").trigger("change");
$l("#splt").on("click", () => $l("#to").val($l("#from").val().split("").join("\u200c")));
$l("#splt").trigger("click");
$l("#anu").on("click", () => {
    window.open(`https://translate.google.com/?sl=ur&tl=hi&text=${encodeURIComponent($l("#to").val())}&op=translate`, "_blank")
});
$l("#lipi").on("click", function () {
    $l(this).remove();
    $lf.getScript("/src/main.js", () => $lf.getScript("/src/lib.js", () => lipi_lekhika()))
    $l("#li").show();
});
$l("#convert").on("click", () => {
    $l("#lipitext").val(LipiLekhikA.parivartak($l("#from").val(), "Urdu", "Normal"));
})