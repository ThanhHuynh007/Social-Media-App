<template>
  <main class="home-view">
    <header class="welcome-header">
      <h1>Chào mừng đến với Wey</h1>
      <p>Giữ liên lạc với bạn bè và thế giới xung quanh bạn.</p>
    </header>

    <section class="post-feed">
      <h2>Bài viết mới nhất</h2>
      <transition-group name="post" tag="div" class="post-list">
        <div v-for="post in posts" :key="post.id" class="post">
          <img :src="post.image" alt="Hình ảnh bài viết" class="post-image"/>
          <h3>{{ post.title }}</h3>
          <p>{{ post.content }}</p>
          <div class="post-footer">
            <small>Đăng bởi {{ post.author }}</small>
            <div class="post-actions">
              <i class="fas fa-heart"></i>
              <i class="fas fa-comment"></i>
            </div>
          </div>
        </div>
      </transition-group>
    </section>
  </main>
</template>

<script>
import post1 from '@/assets/post1.jpg';
import post2 from '@/assets/post2.jpg';

export default {
  name: 'home',
  data() {
    return {
      posts: [
        { id: 1, title: 'Xin chào thế giới', content: 'Đây là bài viết đầu tiên trên Wey!', author: 'Admin', image: post1 },
        { id: 2, title: 'Vue.js rất tuyệt', content: 'Xây dựng các thành phần với Vue.js rất thú vị!', author: 'User123', image: post2 },
        // Thêm nhiều bài viết hơn nếu cần
      ]
    }
  }
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

.home-view {
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f0f2f5;
}

.welcome-header {
  text-align: center;
  margin-bottom: 20px;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 10px;
}

p {
  font-size: 1.2em;
  color: #555;
}

.post-feed {
  margin-top: 20px;
}

.post-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.post {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin: 10px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;
  width: 750px; /* Chỉnh kích thước của bài viết */
  text-align: center;
}

.post:hover {
  transform: translateY(-5px);
}

.post-image {
  width: 100%;
  height: auto;
  border-radius: 10px;
  margin-bottom: 10px;
}

.post-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.post-actions i {
  cursor: pointer;
  margin-left: 10px;
  color: #555;
}

.post-actions i:hover {
  color: #000;
}

.post-enter-active, .post-leave-active {
  transition: opacity 0.5s;
}

.post-enter, .post-leave-to /* .post-leave-active in <2.1.8 */ {
  opacity: 0;
}

.post-move {
  transition: transform 0.5s;
}
</style>
