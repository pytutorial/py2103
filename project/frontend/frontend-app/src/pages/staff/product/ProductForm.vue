<template>
    <div id="app" class="container mt-3">
        <form id="fmt" @submit.prevent="save()" class="col-9">
            <table class="table">
                <tbody>
                    <tr>
                        <td><label>Mã:</label></td>
                        <td><input class="form-control" name="code"></td>
                    </tr>
                    <tr>
                        <td><label>Tên:</label></td>
                        <td><input class="form-control" name="name"></td>
                    </tr>
                    <tr>
                        <td><label>Mô tả:</label></td>
                        <td><textarea class="form-control" name="description"></textarea></td>
                    </tr>
                    <tr>
                        <td><label>Đơn giá:</label></td>
                        <td><input class="form-control" name="price"></td>
                    </tr>
                    <tr>
                        <td><label>Ảnh:</label></td>
                        <td><input type='file' class="form-control-file" name="image"></td>
                    </tr>
                </tbody>
            </table>
            
            <button class="btn btn-primary">Lưu lại</button>
        </form>
    </div>
</template>
<script>
export default {
    data: () => ({
        name: "",
    }),
    methods: {
        save: async function(){
            let data = new FormData(document.getElementById('fmt'));
            console.log(data.get('name'), data.get('code'));
        }
    },
    mounted: function(){
        
    }
}
</script>
