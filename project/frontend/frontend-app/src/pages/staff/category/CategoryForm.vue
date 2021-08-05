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
                </tbody>
            </table>
            
            <button class="btn btn-primary">Lưu lại</button>
        </form>
    </div>
</template>
<script>
export default{
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
