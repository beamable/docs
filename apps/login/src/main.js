import { mount } from 'svelte'
import App from './App.svelte'

function bind(element, props, callback){
  const app = mount(App, {
    target: element,
    props: {
      title: props.title,
      showTitle: props.showTitle ?? true,
      callback: callback
    }
  })
}
export default {
  bind
}