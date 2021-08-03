<template>
  <div>
    <component-1></component-1>
    <component-2></component-2>
    {{x}}
  </div>
</template>

<script>
import Component1 from "./components/Component1.vue";
import Component2 from "./components/Component2.vue";

export default {
  components: {Component1, Component2},
  data: function(){ return {x: 1} }
}
</script>
