// 샘플 게임 데이터
const gameData = [
    {
        title: "사이버펑크 2077",
        genre: "RPG",
        imageUrl: "https://placehold.co/400x300/FFD700/000000?text=Cyberpunk"
    },
    {
        title: "The Witcher 3: Wild Hunt",
        genre: "RPG",
        imageUrl: "https://placehold.co/400x300/DC143C/FFFFFF?text=Witcher+3"
    },
    {
        title: "Grand Theft Auto V",
        genre: "액션 어드벤처",
        imageUrl: "https://placehold.co/400x300/20B2AA/FFFFFF?text=GTA+V"
    },
    {
        title: "League of Legends",
        genre: "MOBA",
        imageUrl: "https://placehold.co/400x300/4682B4/FFFFFF?text=LoL"
    },
    {
        title: "배틀그라운드",
        genre: "배틀로얄",
        imageUrl: "https://placehold.co/400x300/FFA500/000000?text=PUBG"
    },
    {
        title: "Overwatch 2",
        genre: "FPS",
        imageUrl: "https://placehold.co/400x300/FFFFFF/000000?text=Overwatch+2"
    },
    {
        title: "원신",
        genre: "RPG",
        imageUrl: "https://placehold.co/400x300/ADD8E6/000000?text=Genshin"
    },
    {
        title: "Alan Wake 2",
        genre: "서바이벌 호러",
        imageUrl: "https://placehold.co/400x300/36454F/FFFFFF?text=Alan+Wake+2"
    }
];

// DOM이 로드된 후 실행
document.addEventListener('DOMContentLoaded', () => {
    const gameListContainer = document.getElementById('game-list-container');

    if (gameListContainer) {
        gameData.forEach(game => {
            const cardCol = document.createElement('div');
            cardCol.className = 'col';

            cardCol.innerHTML = `
                <div class="card h-100">
                    <img src="${game.imageUrl}" class="card-img-top" alt="${game.title}">
                    <div class="card-body">
                        <h5 class="card-title">${game.title}</h5>
                        <p class="card-text text-muted">${game.genre}</p>
                        <a href="#" class="btn btn-primary">더 보기</a>
                    </div>
                </div>
            `;
            gameListContainer.appendChild(cardCol);
        });
    }
});
