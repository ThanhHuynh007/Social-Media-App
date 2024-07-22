# wey_frontend

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
### Cài đặt Backend

1. **Clone Repository**

    ```bash
    git clone https://github.com/ThanhHuynh007/Social-Media-App.git
    cd Social-Media-App
    ```

2. **Tạo và kích hoạt môi trường ảo**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```

3. **Cài đặt các yêu cầu**

    ```bash
    pip install -r requirements.txt
    ```

4. **Chạy migrations**

    ```bash
    python manage.py migrate
    ```

5. **Chạy máy chủ phát triển**

    ```bash
    python manage.py runserver
    ```

    Dự án sẽ chạy tại `http://127.0.0.1:8000`.

### Cài đặt Frontend

1. **Chuyển đến thư mục frontend**

    ```bash
    cd frontend
    ```

2. **Cài đặt các phụ thuộc**

    ```bash
    npm install  # Hoặc sử dụng yarn: yarn install
    ```

3. **Chạy máy chủ phát triển**

    ```bash
    npm run serve  # Hoặc sử dụng yarn: yarn serve
    ```

    Frontend sẽ chạy tại `http://localhost:5173`.

    ## Tài liệu tham khảo

- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/)
- [Vue.js Documentation](https://vuejs.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)