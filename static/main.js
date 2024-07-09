async function moveArm(direction) {
    const response = await fetch('/move_arm', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ direction })
    });
    const position = await response.json();
    document.getElementById('position').innerText = `x: ${position.x}, y: ${position.y}, z: ${position.z}`;
}
