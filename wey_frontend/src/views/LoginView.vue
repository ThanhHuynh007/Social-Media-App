<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Đăng nhập</h1>

                <p class="mb-6 text-gray-500">
                    Chào mừng trở lại! Vui lòng đăng nhập vào tài khoản Wey của bạn để tiếp tục kết nối với bạn bè, chia sẻ nội dung và khám phá cộng đồng. Nếu bạn chưa có tài khoản,
                </p>

                <p class="font-bold">
                    Chưa có tài khoản? <RouterLink :to="{'name': 'signup'}" class="underline">Nhấn vào đây</RouterLink> để tạo một tài khoản mới!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Email</label><br>
                        <input type="email" v-model="form.email" placeholder="Địa chỉ email của bạn" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Mật khẩu</label><br>
                        <input type="password" v-model="form.password" placeholder="Mật khẩu của bạn" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Đăng nhập</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Email của bạn còn thiếu')
            }

            if (this.form.password === '') {
                this.errors.push('Mật khẩu của bạn còn thiếu')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)

                        this.errors.push('Email hoặc mật khẩu không chính xác! Hoặc tài khoản chưa được kích hoạt!')
                    })
            }
            
            if (this.errors.length === 0) {
                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>
