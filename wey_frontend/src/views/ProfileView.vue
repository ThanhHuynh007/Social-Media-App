<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full" alt="User Avatar">
                
                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{name: 'friends', params: {id: user.id}}" class="text-xs text-gray-500">{{ user.friends_count }} Bạn bè</RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} Bài đăng</p>
                </div>

                <div class="mt-6 space-y-4">
                    <div class="flex justify-center space-x-2">
                        <button 
                            class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                            @click="sendFriendshipRequest"
                            v-if="userStore.user.id !== user.id && can_send_friendship_request"
                            id="send-friendship-request"
                        >
                            Kết bạn
                        </button>

                        <button 
                            class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                            @click="sendDirectMessage"
                            v-if="userStore.user.id !== user.id"
                            id="send-direct-message"
                        >
                            Nhắn tin
                        </button>
                    </div>

                    <div class="flex justify-center space-x-2">
                        <RouterLink 
                            class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                            to="/profile/edit"
                            v-if="userStore.user.id === user.id"
                            id="edit-profile"
                        >
                            Sửa profile
                        </RouterLink>

                        <button 
                            class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg" 
                            @click="logout"
                            v-if="userStore.user.id === user.id"
                            id="logout"
                        >
                            Đăng xuất
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
            >
                <FeedForm 
                    v-bind:user="user" 
                    v-bind:posts="posts"
                />
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" v-on:deletePost="deletePost"/>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />

            <Trends />
        </div>
    </div>
</template>

<style>
input[type="file"] {
    display: none;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
</style>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import FeedForm from '../components/FeedForm.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
        FeedForm
    },

    data() {
        return {
            posts: [],
            user: {
                id: ''
            },
            can_send_friendship_request: null,
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },

        sendDirectMessage() {
            console.log('sendDirectMessage')

            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/chat')
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    this.can_send_friendship_request = false

                    if (response.data.message == 'request already sent') {
                        this.toastStore.showToast(5000, 'Đã gửi yêu cầu!', 'bg-red-300')
                    } else {
                        this.toastStore.showToast(5000, 'Yêu cầu đã được gửi!', 'bg-emerald-300')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.can_send_friendship_request = response.data.can_send_friendship_request
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            console.log('Đăng xuất')

            this.userStore.removeToken()

            this.$router.push('/login')
        }
    }
}
</script>
