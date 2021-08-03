<template>
    <div><button @click="btnClick()">Increase</button></div>
</template>
<script>
export default {
    methods: {
        btnClick: function() {this.$store.commit('increment');}
    }
}
</script>
