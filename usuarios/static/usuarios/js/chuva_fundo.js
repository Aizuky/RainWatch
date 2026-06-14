document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("rainBackground");
    
    // Densidade da chuva (pode aumentar ou diminuir a quantidade aqui)
    const dropCount = 130; 

    for (let i = 0; i < dropCount; i++) {
        const drop = document.createElement("div");
        drop.classList.add("background-drop");

        // Espalha as gotas lateralmente de forma randômica
        drop.style.left = `${Math.random() * 100}%`;
        const duration = 0.6 + Math.random() * 1.0;
        drop.style.animationDuration = `${duration}s`;
        drop.style.animationDelay = `${Math.random() * 2}s`;
        drop.style.opacity = 0.1 + Math.random() * 0.4;

        container.appendChild(drop);
    }
});