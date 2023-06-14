function carregar() {
    var msg = window.document.getElementById('msg')
    var pic = window.document.getElementById('pic')
    var dt = new Date()
    var hr = dt.getHours()


    msg.innerHTML = `Now is ${hr} hours`;

    if (hr >= 0 && hr < 12) {
        // bom dia
        pic.src = 'morning.png'
        document.body.style.background = '#efc586'
    } else if (hr >= 12 && hr <= 18) {
        // boa tarde
        pic.src = 'afternoon.png'
        document.body.style.background = '#e0783c'
    } else {
        // boa noite
        pic.src = 'evening.png'
        document.body.style.background = '#4B3E64'
    }
};
