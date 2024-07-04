try{
    document.getElementsByClassName('owl-prev').item(0).remove()
    document.getElementsByClassName('owl-next').item(0).remove()
}
catch{
    console.warn("ERR01")
}