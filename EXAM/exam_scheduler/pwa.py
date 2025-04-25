import streamlit as st
from streamlit.components.v1 import html

def setup_pwa():
    """Injects PWA required tags and service worker registration"""
    pwa_js = """
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js')
                    .then(reg => console.log('Service Worker registered'))
                    .catch(err => console.log('Service Worker registration failed: ', err));
            });
        }
    </script>
    """
    html(pwa_js)

def set_pwa_meta():
    """Sets PWA meta tags"""
    meta_html = """
    <link rel="manifest" href="/manifest.json">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#4b8bf5"/>
    """
    html(meta_html)
