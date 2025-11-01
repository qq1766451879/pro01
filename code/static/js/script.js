// 创建粒子效果
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // 随机位置
        particle.style.left = Math.random() * 100 + 'vw';
        particle.style.top = Math.random() * 100 + 'vh';
        
        // 随机大小
        const size = Math.random() * 3 + 1;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        
        // 随机颜色
        const colors = ['#00c6ff', '#0072ff', '#3b82f6', '#00d1b2'];
        particle.style.background = colors[Math.floor(Math.random() * colors.length)];
        
        // 随机动画延迟
        particle.style.animationDelay = Math.random() * 5 + 's';
        particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
        
        particlesContainer.appendChild(particle);
    }
}

// 步骤切换函数
function showStep(stepNumber) {
    // 隐藏所有步骤
    document.querySelectorAll('.step').forEach(step => {
        step.classList.remove('active');
    });
    
    // 显示指定步骤
    document.getElementById(`step${stepNumber}`).classList.add('active');
}

// 进度条动画函数 - 优化为更快速版本
function animateProgress(progressBar, progressText, targetPercent, duration = 300) {
    return new Promise(resolve => {
        let currentPercent = 0;
        const increment = targetPercent / (duration / 20); // 更快的更新频率
        
        const timer = setInterval(() => {
            currentPercent += increment;
            if (currentPercent >= targetPercent) {
                currentPercent = targetPercent;
                clearInterval(timer);
                resolve();
            }
            
            progressBar.style.width = currentPercent + '%';
            progressText.textContent = Math.round(currentPercent) + '%';
        }, 20); // 更短的间隔时间
    });
}

// 分析过程函数 - 优化为更快速版本
async function startAnalysis() {
    const stockName = document.getElementById('stockInput').value.trim();
    
    if (!stockName) {
        // 输入框抖动效果
        const input = document.getElementById('stockInput');
        input.style.animation = 'shake 0.5s ease-in-out';
        setTimeout(() => {
            input.style.animation = '';
        }, 500);
        input.focus();
        return;
    }
    
    // 设置结果中的股票名称
    document.querySelector('.sName').textContent = stockName;
    
    // 切换到分析中步骤
    showStep(2);
    
    // 模拟分析过程 - 大幅缩短时间
    await animateProgress(
        document.getElementById('progress1'),
        document.getElementById('progress1Text'),
        100,
        250 // 从400ms缩短到250ms
    );
    
    await animateProgress(
        document.getElementById('progress2'),
        document.getElementById('progress2Text'),
        100,
        250 // 从400ms缩短到250ms
    );
    
    await animateProgress(
        document.getElementById('progress3'),
        document.getElementById('progress3Text'),
        100,
        250 // 从400ms缩短到250ms
    );
    
    // 延迟一下然后显示结果 - 缩短延迟时间
    setTimeout(() => {
        showStep(3);
    }, 200); // 从300ms缩短到200ms
}

// 事件监听器
document.addEventListener('DOMContentLoaded', function() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const stockInput = document.getElementById('stockInput');
    
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', startAnalysis);
    }
    
    if (stockInput) {
        stockInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                if (analyzeBtn) {
                    analyzeBtn.click();
                }
            }
        });
    }
    
    // 页面加载时创建粒子
    createParticles();
    
    // 自动聚焦到输入框
    if (stockInput) {
        stockInput.focus();
    }
});

// 添加抖动动画
const style = document.createElement('style');
style.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
    }
`;
document.head.appendChild(style);