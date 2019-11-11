<template>
  <div id="app">
    <!-- if 만약 inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨s.  -->
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VidoeList'
import VideoDetail from './components/VideoDetail'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY // 어디에 들어있는지 
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',  
  data() {
    return { // 오브젝트를 리턴하는 함수를 써야합니다.
      videos: [], 
      selectedVideo: null,
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onVideoSelect(video) {
      this.selectedVideo = video
    },

    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        },
      })
      .then(response => {
        
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
