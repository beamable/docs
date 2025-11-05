// localStore.js
import { writable } from 'svelte/store';

export function localStore(key, initialValue) {
  // Try to read from localStorage
  const storedValue = localStorage.getItem(key);
  const data = storedValue ? JSON.parse(storedValue) : initialValue;

  const store = writable(data);

  // Subscribe to changes and save to localStorage
  store.subscribe(value => {
    localStorage.setItem(key, JSON.stringify(value));
  });

  return store;
}
