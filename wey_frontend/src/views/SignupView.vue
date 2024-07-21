<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Đăng ký</h1>

                <p class="mb-6 text-gray-500">
                    Chào mừng bạn đến với Wey, ứng dụng mạng xã hội mới! Tạo tài khoản để kết nối với bạn bè, chia sẻ những khoảnh khắc và khám phá nội dung thú vị từ cộng đồng. Hãy gia nhập Wey ngay hôm nay để không bỏ lỡ bất kỳ điều gì!
                </p>

                <p class="font-bold">
                    Bạn đã có tài khoản? <RouterLink :to="{'name': 'login'}" class="underline">Nhấn vào đây</RouterLink> để đăng nhập!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Tên</label><br>
                        <input type="text" v-model="form.name" placeholder="Họ và tên " class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Địa chỉ e-mail " class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Mật khẩu</label><br>
                        <input type="password" v-model="form.password1" placeholder="Mật khẩu " class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Nhập lại mật khẩu</label><br>
                        <input type="password" v-model="form.password2" placeholder="Nhập lại mật khẩu " class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Đăng ký</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('E-mail của bạn còn thiếu')
            }

            if (this.form.name === '') {
                this.errors.push('Tên của bạn còn thiếu')
            }

            if (this.form.password1 === '') {
                this.errors.push('Mật khẩu của bạn còn thiếu')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('Mật khẩu không khớp')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Người dùng đã được đăng ký. Vui lòng kích hoạt tài khoản của bạn bằng cách nhấp vào liên kết trong email.', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Đã xảy ra lỗi. Vui lòng thử lại', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>
