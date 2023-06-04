const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

const PLAYER_STORAGE_KEY = 'Dung_dz'

const cd = $('.cd');
const heading = $('header h2');
const cdThumb = $('.cd-thumb');
const audio = $('#audio');
const playBtn = $('.btn-toggle-play')
const player = $('.player')
const progress = $('#progress')
const nextBtn = $('.btn-next');
const prevBtn = $('.btn-prev');
const randomBtn = $('.btn-random')
const repeatBtn = $('.btn-repeat')
const playList = $('.playlist');



 
const app = {
    currentIndex: 0,
    isPlaying: false,
    isRandom: false,
    isRepeat: false,
    config: JSON.parse(localStorage.getItem(PLAYER_STORAGE_KEY)) || {},

    songs: [
        {
            name: 'Yếu đuối',
            singer: 'Dung dz',
            path: '/Javascript/CacBaiThucHanh/assets/music/YeuDuoi-QuangDangTran-6690099.mp3',
            image: '/Javascript/CacBaiThucHanh/assets/img/img1.jpg'
        },
        {
            name: 'Ngày mai em đi mất',
            singer: 'Dung dz',
            path: '/Javascript/CacBaiThucHanh/assets/music/NgayMaiEmDiMat-KhaiDangDatG-7747861.mp3',
            image: '/Javascript/CacBaiThucHanh/assets/img/img2.jpg'
        },
        {
            name: 'Roi ta se ngam phao hoa cung nhau',
            singer: 'Dung dz',
            path: '/Javascript/CacBaiThucHanh/assets/music/RoiTaSeNgamPhaoHoaCungNhau-OlewVietNam-8485329.mp3',
            image: '/Javascript/CacBaiThucHanh/assets/img/img3.jpg'
        },
        {
            name: 'Roi ta se ngam phao hoa cung nhau',
            singer: 'Dung dz',
            path: '/Javascript/CacBaiThucHanh/assets/music/RoiTaSeNgamPhaoHoaCungNhau-OlewVietNam-8485329.mp3',
            image: '/Javascript/CacBaiThucHanh/assets/img/img3.jpg'
        },
        {
            name: 'Roi ta se ngam phao hoa cung nhau',
            singer: 'Dung dz',
            path: '/Javascript/CacBaiThucHanh/assets/music/RoiTaSeNgamPhaoHoaCungNhau-OlewVietNam-8485329.mp3',
            image: '/Javascript/CacBaiThucHanh/assets/img/img3.jpg'
        },
        {
            name: 'Roi ta se ngam phao hoa cung nhau',
            singer: 'Dung dz',
            path: '/Javascript/CacBaiThucHanh/assets/music/RoiTaSeNgamPhaoHoaCungNhau-OlewVietNam-8485329.mp3',
            image: '/Javascript/CacBaiThucHanh/assets/img/img3.jpg'
        },
    ],



    setConfig: function(key, value) {
        this.config[key] = value;
        localStorage.setItem(PLAYER_STORAGE_KEY, JSON.stringify(this.config))
    },

    render: function() {
        const htmls = this.songs.map((song, index) => {
            return `
            <div class="song ${index === this.currentIndex ? 'active' : ''}" data-index = ${index}> 
                <div class="thumb" style="background-image: url('${song.image}')">
                </div>
                <div class="body">
                    <h3 class="title">${song.name}</h3>
                    <p class="author">${song.singer}</p>
                </div>
                <div class="option">
                    <i class="fas fa-ellipsis-h"></i>
                </div>
            </div>
            `;
        });
        playList.innerHTML = htmls.join('');
    },

    defineProperties: function(){
        Object.defineProperty(this, 'currentSong', {
            get: function() {
                return this.songs[this.currentIndex]
            }
        })
    },

    handleEvent: function() {
        const _this = this;
        const cdWidth = cd.offsetWidth;
        
        // Xử lý CD quay / dừng
        const cdThumbAnimate = cdThumb.animate([
            {
                transform: 'rotate(360deg)'
            }
        ], {
            duration: 10000,
            interation: Infinity,
        });
        cdThumbAnimate.pause()


        // Xử lý phóng to hoặc thu nhỏ cd
        document.onscroll = function() {
            const scrollY = window.scrollY;
            const newCdWidth = cdWidth - scrollY


            cd.style.width = newCdWidth > 0 ? newCdWidth + 'px' : 0
            cd.style.opacity = newCdWidth / cdWidth;
        }

        // Xử lý khi click play

        playBtn.onclick = function() {
            if ( _this.isPlaying){
                audio.pause()
            } else {
               audio.play()
            }
        }

        // Khi song được play
        audio.onplay = function() {
            _this.isPlaying = true;
            player.classList.add('playing')
            cdThumbAnimate.play();
        }
          // Khi song được pause
          audio.onpause = function() {
            _this.isPlaying = false;
            player.classList.remove('playing')
            cdThumbAnimate.pause();
        }

        // Khi tien do bai hat thay doi
        audio.ontimeupdate = function() {
            if (audio.duration) {
                const progressPercent = Math.floor(audio.currentTime / audio.duration * 100);
                progress.value = progressPercent
            }
        }

        // Khi tua song
        progress.oninput = function(e) {
            const seekTime = e.target.value * audio.duration / 100;
            audio.currentTime = seekTime;

        }


        

        // Khi next song
        nextBtn.onclick = function() {
            if (_this.isRandom){
                _this.playRandomSong()
            } else {
                _this.nextSong();
            }
            audio.play();
            _this.render();
            _this.scrollActiveSong();

        };
        prevBtn.onclick = function() {
            if (_this.isRandom){
                _this.playRandomSong()
            } else {
                _this.prevSong();
                
            }
            audio.play();
            _this.render();
            _this.scrollActiveSong();

        };

        // Xử lý bật tắt random
        randomBtn.onclick = function(e) {
            _this.isRandom = !_this.isRandom;
            _this.setConfig('isRandom', _this.isRandom);
            randomBtn.classList.toggle('active', _this.isRandom)
            
        };

        // Xử lý lặp lại song
        repeatBtn.onclick = function(e) {
            _this.isRepeat = !_this.isRepeat;
            _this.setConfig('isRepeat', _this.isRepeat);
            repeatBtn.classList.toggle('active', _this.repeatBtn)
        }

        // Xử lý next song khi audio end
        audio.onended = function() {
            if (_this.isRepeat) {
                audio.play()
            } else {
                nextBtn.click()
            }
        }

        // Lăng nghe hành vi click vào playlist
        
        playList.onclick = function(e) {
            const songNode = e.target.closest('.song:not(.active)')

            if (songNode || e.target.closest('.option')){
                // Xử lý khi click vào song
                if (songNode) {
                    _this.currentIndex = Number(songNode.dataset.index)
                    _this.loadCurrentSong();
                    _this.render();
                    audio.play();
                }

                // Xử lý khi click vào option
                if (e.target.closest('.option')) {

                }
            }
        }

    },

    scrollActiveSong: function() {
        setTimeout(() => {
            $('.song.active').scrollIntoView({
                behavior: 'smooth',
                block: 'nearest',
            })
        }, 300)
    },

    loadCurrentSong: function() {
        heading.textContent  = this.currentSong.name
        cdThumb.style.backgroundImage = `url('${this.currentSong.image}')`
        audio.src = this.currentSong.path

    },

    loadConfig: function() {
        this.isRandom = this.config.isRandom;
        this.isRepeat = this.config.isRepeat;
    },

    nextSong: function(){
        this.currentIndex++;
        if(this.currentIndex >= this.songs.length) {
            this.currentIndex = 0;
        }
        this.loadCurrentSong()
    },
    prevSong: function(){
        this.currentIndex--;
        if(this.currentIndex < 0) {
            this.currentIndex = this.songs.length - 1;
        }
        this.loadCurrentSong()
    },

    playRandomSong: function(){
        let newIndex;
        do {
            newIndex = Math.floor(Math.random() * this.songs.length)
        } while (newIndex === this.currentIndex)

        this.currentIndex = newIndex
        this.loadCurrentSong()
    },
 
   
    start: function() {
        
        // Gán cấu hình từ config vào app
        this.loadConfig()
        // Định nghĩa các thuộc tính cho Object
        this.defineProperties();

        // Lắng nghe / xử lý sự kiện (Dom Event)
        this.handleEvent();
        
        // Render playlist
        this.render();

        // Tải thông tin bài hát đầu tiên vào UI khi chạy ứng dụng
        this.loadCurrentSong();

        // Hiển thị trạng thái ban đầu của btn repeat và random
        randomBtn.classList.toggle('active', this.isRandom)
        repeatBtn.classList.toggle('active', this.repeatBtn)
    }
};

app.start();