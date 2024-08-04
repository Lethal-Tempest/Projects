async function getSingers() {
    let a=await fetch("http://192.168.0.111:8000/songs/")
    let result=await a.text();
    let div=document.createElement("div");
    div.innerHTML=result;
    let as=div.getElementsByTagName("a");
    let singers=[];
    for(let i=0;i<as.length;i++){
        let singerUrl = new URL(as[i].getAttribute('href'), a.url).href;
        singers.push(singerUrl);
    }
    return singers;
}

async function getSingerPic(singerName){
    let singers=await getSingers();
    for(let i=0;i<singers.length;i++){
        if(singers[i].split("/songs/")[1].replace("%20"," ").replace("/","")==singerName){
            let a=await fetch(singers[i])
            let result=await a.text();
            let div=document.createElement("div");
            div.innerHTML=result;
            let as=div.getElementsByTagName("a");
            let songs=[];
            for(let i=0;i<as.length;i++){
                if(as[i].href.includes("cover_pic")){
                    let songUrl = new URL(as[i].getAttribute('href'), a.url).href;
                    return (songUrl);
                }
            }
        }
    }
}

async function getSongs(singerName){
    let singers=await getSingers();
    for(let i=0;i<singers.length;i++){
        if(singers[i].split("/songs/")[1].replace("%20"," ").replace("/","")==singerName){
            let a=await fetch(singers[i])
            let result=await a.text();
            let div=document.createElement("div");
            div.innerHTML=result;
            let as=div.getElementsByTagName("a");
            let songs=[];
            for(let i=0;i<as.length;i++){
                if(!(as[i].href.includes("cover_pic"))){
                    let newData=new URL(as[i].getAttribute('href'), a.url).href;
                    let a2=await fetch(newData);
                    let result2=await a2.text();
                    let div2=document.createElement("div");
                    div2.innerHTML=result2;
                    let as2=div2.getElementsByTagName("a");
                    for(let j=0;j<as2.length;j++){
                        if(as2[j].href.endsWith(".mp3")){
                            let songUrl = new URL(as2[j].getAttribute('href'), a2.url).href;
                            songs.push(songUrl);
                        }
                    }
                }
            }
            return songs;
        }
    }
}

async function getSongPic(songName, singerName){
    let songs=await getSongs(singerName);
    for(let i=0;i<songs.length;i++){
        if(songs[i].includes(songName.replaceAll(" ","%20"))){
            return((songs[i].replaceAll(`/${songName.replaceAll(" ", "%20")}.mp3`,"")).concat("/cover_pic.jpeg"))
        }
    }
}

let currentSong = new Audio()
let bttn=document.getElementById("play");
let songName=document.getElementsByClassName("song_name")[0];
let timeElapsed=document.getElementsByClassName("time_elapsed")[0];
let timeRemaining=document.getElementsByClassName("time_remaining")[0];
let seekBar=document.getElementsByClassName("seekbar")[0];
let seek=document.getElementsByClassName("seek")[0]
let signup=document.getElementsByClassName("sign_up")[0];
let login=document.getElementsByClassName("login")[0];
let arrowDiv=document.getElementsByClassName("arrow_div")[0];
let popAlbums=document.getElementsByClassName("pop_albums")[0];
let flag=1;

function playMusicFromLib(track){
    currentSong.src=track;
    currentSong.play();  
    bttn.src="img/pause.svg"
    let song_name=track.split("/songs/")[1];
    song_name=song_name.replaceAll("%20", " ");
    song_name=song_name.replace(".mp3", "");
    song_name=song_name.split("/")[1];
    songName.innerText=song_name;
    timeElapsed.innerText="00:00";
    timeRemaining.innerText="00:00"; 
    seek.style.left="0%";
}

function playMusicFromSeekbar(){
    if(currentSong.src!=""){
        if(currentSong.paused){
            currentSong.play();
            bttn.src="img/pause.svg"
        }
        else{
            currentSong.pause();
            bttn.src="img/play.svg"
        }
    }
    else{
        bttn.src="img/pause.svg";
    }
}

function secToMin(sec){
    let min=Math.floor(sec/60);
    sec=Math.floor(sec%60);
    min=String(min).padStart(2, '0');
    sec=String(sec).padStart(2, '0')
    return([min, sec]);
}

async function createSongCard(songName, singerName){
    let cc=document.getElementsByClassName("card_collection")[0];
    let c=document.createElement("div");
    c.className="card";
    let i=document.createElement("img");
    i.src=await getSongPic(songName, singerName);
    i.className="song_pic"
    c.appendChild(i);
    let t=document.createElement("div");
    t.className="card_text";
    c.appendChild(t);
    let n=document.createElement("div");
    n.className="name";
    n.innerText=songName;     
    t.appendChild(n);
    let s=document.createElement("div");
    s.className="singer";
    s.innerText=singerName;  
    t.appendChild(s);
    let gp=document.createElement("div");
    gp.className="green_play";
    c.appendChild(gp);
    let gpl=document.createElement("img");
    gpl.src="try/green_play_button_editted.png";
    gpl.className="green_play_logo";
    gp.appendChild(gpl);
    cc.appendChild(c);
    let songs=await getSongs(singerName);
    c.addEventListener("click", ()=>{
        for(let i=0;i<songs.length;i++){
            if(songs[i].includes(songName.replaceAll(" ","%20"))){
                console.log(songs[i]);
                playMusicFromLib(songs[i]);
                break;
            }
        }
    })
}

let goLeft=document.getElementsByClassName("go_left")[0];
let goRight=document.getElementsByClassName("go_right")[0];
let cc=document.getElementsByClassName("card_collection")[0];
let list=document.getElementsByClassName("lib_list")[0];

arrowDiv.removeChild(goLeft);

goLeft.addEventListener("click", async ()=>{
    popAlbums.innerText="Popular Artists";
    arrowDiv.appendChild(goRight);
    list.innerHTML="";
    cc.innerHTML="";
    let singers=await getSingers();
    for(let i=0;i<singers.length;i++){
        let singer_name=singers[i].split("/songs/")[1].replace("%20"," ").replace("/","");
        createSingerCard(singer_name);
    }
})

let rightPrevSinger="";
if (rightPrevSinger==""){
    arrowDiv.removeChild(goRight);
}

goRight.addEventListener("click", async ()=>{
    let songs = await getSongs(rightPrevSinger);
    list.innerHTML="";
    cc.innerHTML="";
    for(let i=0;i<songs.length;i++){
        let song_name=songs[i].split("/songs/")[1];
        song_name=song_name.replaceAll("%20", " ");
        song_name=song_name.replace(".mp3", "");
        song_name=song_name.split("/")[1];
        let li=document.createElement("li");
        li.innerText=song_name;
        let play_opt=document.createElement("img");
        play_opt.src="try/lib_song_play_button.png";
        play_opt.className="lib_song_play_button";
        play_opt.alt="play";
        li.append(play_opt);
        list.append(li);
        createSongCard(song_name, rightPrevSinger);
    }
})


async function createSingerCard(singerName){
    let c=document.createElement("div");
    c.className="singer_card";
    let i=document.createElement("img");
    i.src=await getSingerPic(singerName);
    i.className="singer_pic"
    c.appendChild(i);
    let t=document.createElement("div");
    t.className="card_text";
    c.appendChild(t);
    let n=document.createElement("div");
    n.className="name";
    n.innerText=singerName;     
    t.appendChild(n); 
    let gp=document.createElement("div");
    gp.className="green_play";
    c.appendChild(gp);
    let gpl=document.createElement("img");
    gpl.src="try/green_play_button_editted.png";
    gpl.className="green_play_logo";
    gp.appendChild(gpl);
    cc.appendChild(c);
    c.addEventListener("click", async ()=>{
        popAlbums.innerText=`Popular Songs by ${singerName}`;
        if(flag==1){
            arrowDiv.appendChild(goLeft)
            flag=0;
        }
        rightPrevSinger=singerName;
        let songs = await getSongs(singerName);
        list.innerHTML="";
        cc.innerHTML="";
        for(let i=0;i<songs.length;i++){
            let song_name=songs[i].split("/songs/")[1];
            song_name=song_name.replaceAll("%20", " ");
            song_name=song_name.replace(".mp3", "");
            song_name=song_name.split("/")[1];
            let li=document.createElement("li");
            li.innerText=song_name;
            let play_opt=document.createElement("img");
            play_opt.src="try/lib_song_play_button.png";
            play_opt.className="lib_song_play_button";
            play_opt.alt="play";
            li.append(play_opt);
            list.append(li);
            createSongCard(song_name, singerName);
        }
        let div=document.getElementsByClassName("lib_songs")[0];
        let song=div.getElementsByTagName("li");
        for(let i=0;i<song.length;i++){
            song[i].addEventListener("click", ()=>{
                playMusicFromLib(songs[i]);
            })
        }
        let playOptions=document.getElementsByClassName("play_options")[0];
        let prev=playOptions.getElementsByTagName("img")[0];
        let play=playOptions.getElementsByTagName("img")[1];
        let next=playOptions.getElementsByTagName("img")[2];
        next.addEventListener("click", ()=>{
            let i=songs.indexOf(currentSong.src)
            if(i<songs.length-1){
                playMusicFromLib(songs[i+1]);
            }
        })
        prev.addEventListener("click", ()=>{
            let i=songs.indexOf(currentSong.src)
            if(i>0){
                playMusicFromLib(songs[i-1]);
            }
        })
        play.addEventListener("click", ()=>{
            playMusicFromSeekbar();
        })
    })
}

async function main() {
    let singers=await getSingers();
    for(let i=0;i<singers.length;i++){
        let singer_name=singers[i].split("/songs/")[1].replace("%20"," ").replace("/","");
        createSingerCard(singer_name);
    }
    currentSong.addEventListener("timeupdate", ()=>{
        let minDone=secToMin(currentSong.currentTime)[0]; 
        let secDone=secToMin(currentSong.currentTime)[1];
        let minLeft=secToMin(currentSong.duration-currentSong.currentTime)[0]; 
        let secLeft=secToMin(currentSong.duration-currentSong.currentTime)[1];
        timeElapsed.innerText=`${minLeft}:${secLeft}`;
        timeRemaining.innerText=`${minDone}:${secDone}`;
        let percentage=(currentSong.currentTime/currentSong.duration)*100;
        seek.style.left = `${percentage}%`;
        if(percentage==100){
            let i=songs.indexOf(currentSong.src)
            if(i<songs.length-1){
                playMusicFromLib(songs[i+1]);
            }
        }
    })
    seekBar.addEventListener("click", e => {
        let offsetX = e.offsetX;
        let width = e.target.getBoundingClientRect().width;
        let percentage = (offsetX / width) * 100;
        if (currentSong.src!="") {
            seek.style.left = `${percentage}%`;
            currentSong.currentTime = (percentage / 100) * currentSong.duration;
        }
    });
    let ham=document.getElementById("ham_div");
    let leftcont=document.getElementsByClassName("left")[0];
    let rightcont=document.getElementsByClassName("right")[0];
    let close=document.getElementsByClassName("close")[0];
    ham.addEventListener("click", ()=>{
        leftcont.style.left="0%";
        leftcont.style.zIndex="1";
        leftcont.style.width= "100%";
        leftcont.style.maxHeight= "100%";
        rightcont.style.left= "100%";
        rightcont.style.width= "0%";
        signup.style.opacity="0";
        login.style.opacity="0";
        close.style.opacity="1";
    })
    close.addEventListener("click", ()=>{
        leftcont.style.left="-100%";
        leftcont.style.width= "0%";
        leftcont.style.maxHeight= "0%";
        rightcont.style.left= "0%";
        rightcont.style.width= "100%";
        signup.style.opacity="1";
        login.style.opacity="1";
    })

    const volumeSlider = document.getElementsByClassName("vol_range")[0];
    const volLogo=document.getElementsByClassName("vol_logo")[0];

    function updateSliderBackground(slider) {
        const value = (slider.value - slider.min) / (slider.max - slider.min) * 100;
        slider.style.setProperty('--slider-value', `${value}%`);
        currentSong.volume=value/100;
        return value;
    }

    updateSliderBackground(volumeSlider);

    volumeSlider.addEventListener('input', function() {
        let val=updateSliderBackground(this);
        if(val==0){
            volLogo.src="img/mute.svg";
        }
        else{
            volLogo.src="img/volume.svg";
        }
    });

    let vol=0;
    volLogo.addEventListener("click", ()=>{
        if(volLogo.src.includes("volume.svg")){
            volLogo.src="img/mute.svg";
            vol=updateSliderBackground(volumeSlider);
            volumeSlider.value=0;
            updateSliderBackground(volumeSlider);
        }
        else{
            volLogo.src="img/volume.svg";
            volumeSlider.value=vol;
            updateSliderBackground(volumeSlider);
        }
    })
}

main();
