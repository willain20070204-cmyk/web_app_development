// 【集中整理區】所有的占卜資料都在這裡，方便後續自行修改！
const fortuneData = [
    {
        name: "🌟 大吉",
        work: "長官賞識，專案順利推進，甚至可能有意外的升遷機會！把握當下展現能力。",
        study: "思緒清晰，學習效率極高。逢考必過，成績突飛猛進。",
        love: "桃花盛開！單身者有望遇見理想對象；有伴者感情升溫，甜蜜無比。",
        money: "財神爺敲門！投資獲利，或有意外之財入帳，錢包滿滿。",
        closing: "現在是你發光發熱的時刻，大膽去實踐夢想吧！"
    },
    {
        name: "✨ 中吉",
        work: "工作穩定發展，付出會得到穩實的回報，適合團隊合作。",
        study: "穩紮穩打，只要按部就班複習，就能獲得理想的成績。",
        love: "有機會透過朋友介紹認識不錯的人；情侶間互動平和溫馨。",
        money: "正財運佳，薪水穩定，小額投資有不錯的收益。",
        closing: "保持平常心，好運水到渠成！順其自然會有好結果。"
    },
    {
        name: "🍀 小吉",
        work: "雖然有些忙碌，但都能順利解決，還能在過程中學到新技能。",
        study: "偶爾會分心，但只要稍微集中注意力，就能突破目前的瓶頸。",
        love: "一個微笑或小舉動就會引來好感，多留意身邊的日常互動。",
        money: "可能有小意外支出，但同時也會有小省錢的幸運時刻。",
        closing: "多留意生活中的小細節，快樂就在身邊！"
    },
    {
        name: "⚖️ 平",
        work: "沒有太多波折，按部就班完成日常工作即可，算是平安的一天。",
        study: "表現中規中矩，維持現狀，不需要給自己太大壓力。",
        love: "感情狀態平靜，順其自然，享受現在的兩人世界或單身步調。",
        money: "收支平衡，守住荷包就是最大的贏家，避免盲目跟風購物。",
        closing: "平凡也是一種幸福，好好休息一下吧！"
    },
    {
        name: "🌧️ 小凶",
        work: "容易與同事發生小摩擦或溝通不良，說話前請多想三秒鐘。",
        study: "可能會遇到較難理解的課題，建議主動多請教老師或同學。",
        love: "容易因小事產生誤會，記得多溝通，不要把話悶在心裡。",
        money: "容易衝動購物，購買前請三思，避免不必要的開銷。",
        closing: "一點小風雨不算什麼，冷靜面對，撐過去就放晴了！"
    },
    {
        name: "⚡ 凶",
        work: "計畫可能生變，需要有備案。處事低調為宜，避免出頭惹事。",
        study: "粗心大意容易出錯，考試或交作業前務必再三檢查。",
        love: "感情容易陷入僵局或冷戰，給彼此一點空間沉澱一下情緒。",
        money: "有破財風險，不宜進行高風險投資或隨意借錢給別人。",
        closing: "逆風飛翔雖然辛苦，但也飛得更高，加油堅持住！"
    },
    {
        name: "🎭 轉機",
        work: "開局充滿挑戰，但只要堅持下去不放棄，就能翻轉局面取得成功。",
        study: "一開始可能會覺得卡關，但多換個角度思考，突然就會茅塞頓開！",
        love: "經歷過磨合與爭吵後，反而能更深入了解對方的想法，感情更穩固。",
        money: "先有支出，後有回報。看準時機再出手，不要太在意一時得失。",
        closing: "黎明前的黑暗最黑，相信自己，曙光即將出現！"
    },
    {
        name: "🚀 飛躍",
        work: "突破舒適圈的好時機，主動爭取新的機會，將有驚奇的發展！",
        study: "對新知識有強烈的渴望，學習新事物會特別順遂，大腦相當活躍。",
        love: "勇敢表達心意，單身者告白成功率高；有伴者可嘗試新的約會模式。",
        money: "憑藉創新想法或發展副業，有機會為你帶來長期額外的收入。",
        closing: "別害怕改變，你比想像中更強大！勇敢跨出那一步。"
    },
    {
        name: "🐢 沉潛",
        work: "目前的環境不適合躁進，多充實自己，耐心等待更好的時機出現。",
        study: "不要急於求成，現在是打好基礎、複習基本功的最好時候。",
        love: "先把重心放在愛自己身上，當你變得更好，就會自然吸引對的人。",
        money: "保守理財為主，建議多把錢投資在健康與自我專業成長上。",
        closing: "蹲下是為了跳得更高，給自己一點喘息空間儲備能量！"
    },
    {
        name: "🎁 奇蹟",
        work: "會接到意想不到的重要任務或合作，為你開啟職場新的一扇窗。",
        study: "無心插柳柳成蔭，考出的成績可能出乎意料的好，運氣極佳。",
        love: "轉角遇到愛！可能在完全沒預料到的場合遇見令人心動的對象。",
        money: "偏財運氣極佳，如果有零錢可以買張彩券碰碰運氣喔！",
        closing: "宇宙為你準備了特別的驚喜，請張開雙手迎接吧！"
    }
];

// 抓取 DOM 元素
const introScreen = document.getElementById('intro-screen');
const loadingScreen = document.getElementById('loading-screen');
const resultScreen = document.getElementById('result-screen');

const drawBtn = document.getElementById('draw-btn');
const resetBtn = document.getElementById('reset-btn');

const resultTitle = document.getElementById('result-title');
const resultWork = document.getElementById('result-work');
const resultStudy = document.getElementById('result-study');
const resultLove = document.getElementById('result-love');
const resultMoney = document.getElementById('result-money');
const resultClosing = document.getElementById('result-closing');

// 顯示特定畫面的函數
function showScreen(screen) {
    // 隱藏所有畫面
    const screens = document.querySelectorAll('.screen');
    screens.forEach(s => {
        s.style.display = 'none';
        s.classList.remove('active');
    });
    
    // 顯示指定畫面
    screen.style.display = 'flex';
    // 些微延遲觸發 opacity 動畫
    setTimeout(() => {
        screen.classList.add('active');
    }, 10);
}

// 抽取運勢的主邏輯
function drawFortune() {
    // 1. 切換到載入畫面 (水晶球動畫)
    showScreen(loadingScreen);

    // 2. 隨機抽選結果
    const randomIndex = Math.floor(Math.random() * fortuneData.length);
    const result = fortuneData[randomIndex];

    // 3. 模擬神秘占卜的計算時間 (2秒)
    setTimeout(() => {
        // 將資料填入結果畫面的對應欄位
        resultTitle.textContent = result.name;
        resultWork.textContent = result.work;
        resultStudy.textContent = result.study;
        resultLove.textContent = result.love;
        resultMoney.textContent = result.money;
        resultClosing.textContent = result.closing;

        // 重置結果卡片的動畫以便下次重新播放
        const card = document.querySelector('.result-card');
        card.style.animation = 'none';
        card.offsetHeight; // 觸發瀏覽器重繪 (Reflow)
        card.style.animation = null; 

        // 顯示結果畫面
        showScreen(resultScreen);
        
    }, 2000);
}

// 綁定按鈕事件
drawBtn.addEventListener('click', drawFortune);

resetBtn.addEventListener('click', () => {
    // 回到首頁並將捲軸移到最上層
    showScreen(introScreen);
    window.scrollTo(0, 0);
});

// 初始化：確保一開始只顯示首頁
showScreen(introScreen);
