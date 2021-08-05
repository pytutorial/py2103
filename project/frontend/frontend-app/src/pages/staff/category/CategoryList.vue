<template>
    <div id='app' class="container mt-3">
        <div class="row">
            <div class="col">
                <a href='category_form.html' class="btn btn-primary float-right">Thêm sản phẩm</a>
            </div>
        </div>

        <table class="table table-bordered mt-3">
            <thead>
                <tr>
                    <th>STT</th>
                    <th>Mã</th>
                    <th>Tên</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
export default{
    data: () => ({
        keyword: "",
        page: 1,
        total: 0,
        items: [],
        pageSize: 5,
        baseUrl: 'http://127.0.0.1:8000'
    }),
    methods: {
        fetch_data: async function(){
        }
    },
    mounted: async function(){
        this.fetch_data()
    }
}
</script>
