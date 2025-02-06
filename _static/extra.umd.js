!function(e,t){"object"==typeof exports&&"undefined"!=typeof module?module.exports=t():"function"==typeof define&&define.amd?define(t):(e="undefined"!=typeof globalThis?globalThis:e||self).Extra=t()}(this,(function(){"use strict";class e{constructor(e,t){if(this.$,"string"==typeof e){if(this.$=document.createElement(e),"object"==typeof t)for(const e in t)e in this.$?this.$[e]=t[e]:this.$.dataset[e]=t[e]}else this.$=e}cloneNode(t){return new e(this.$.cloneNode(t))}set innerText(e){this.$.innerText=e}get innerText(){return this.$.innerText}get height(){return this.$.offsetHeight}get width(){return this.$.offsetWidth}get id(){return this.$.id}set id(e){this.$.id=e}get value(){return this.$.value}set value(e){this.$.value=e}get src(){return this.$.src}set src(e){this.$.src=e}focus(){this.$.focus()}get classList(){return this.$.classList}get style(){return this.$.style}onchange(e,t,n){return this.$.onchange=r=>{void 0===n?t.apply(e,[r]):n.constructor==Array&&(n.push(r),t.apply(e,n))},this}onclick(e,t,n){return this.$.onclick=r=>{void 0===n?t.apply(e,[r]):n.constructor==Array&&(n.push(r),t.apply(e,n))},this}onup(e,t,n){return this.$.addEventListener("mouseup",(r=>{void 0===n?t.apply(e,[r]):n.constructor==Array&&(n.push(r),t.apply(e,n))})),this}ondown(e,t,n){return this.$.addEventListener("mousedown",(r=>{void 0===n?t.apply(e,[r]):n.constructor==Array&&(n.push(r),t.apply(e,n))})),this}onmove(e,t,n){return this.$.addEventListener("mousemove",(r=>{void 0===n?t.apply(e,[r]):n.constructor==Array&&(n.push(r),t.apply(e,n))})),this}onevent(e,t,n,r){return this.$.addEventListener(e,(e=>{void 0===r?n.apply(t,[e]):r.constructor==Array&&(r.push(e),n.apply(t,r))})),this}append(e){return e.constructor!=Array&&(e=[e]),e.forEach((e=>{/HTML(.*)Element/.test(e.constructor.name)?this.$.appendChild(e):"object"==typeof e&&/HTML(.*)Element/.test(e.$.constructor.name)&&this.$.appendChild(e.$)})),this}delete(){this.$.remove()}removeChilds(){let e=this.$.lastElementChild;for(;e;)this.$.removeChild(e),e=this.$.lastElementChild;return this}static get(t,n){return void 0===(n=n instanceof e?n.$:n)?document.querySelector(t):n.querySelector(t)}static getAll(t,n){return"object"==typeof(n=n instanceof e?n.$:n)?n.querySelectorAll(t):get(n).querySelectorAll(t)}static switchState(t,n){let r=null!=n?n:"on";(t=t instanceof e?t.$:t).classList.contains(r)?t.classList.remove(r):t.classList.add(r)}static UID(){return(+new Date).toString(36)+Math.random().toString(36).substr(2)}static prototypeDetails(t){let n=new e("summary",{innerText:t.innerText}),r=new e("details",{id:t.id,name:t.id}).append(n);return null!=t.onevent&&t.onevent.forEach((e=>{e.args.push(r.$),n.onevent(e.event,e.self,e.fun,e.args)})),r}static prototypeInputFile(t){return new e("label",{htmlFor:`${t.id}_input`,id:t.id,className:t.className,innerText:t.innerText}).append(new e("input",{id:`${t.id}_input`,type:"file"}))}static prototypeCheckSwitch(t){let n=new e("input",{id:t.id,name:t.id,className:"checkswitch",type:"checkbox",value:!1});return[n,new e("div",{className:t.className}).append([new e("div").append([new e("label",{className:"checkswitch",htmlFor:t.id,innerText:t.innerText}).append([n,new e("span")])])])]}static prototypeDownload(e,t){let n,r=/.*\.(py|xml|csv|json|svg|png)$/;if(!r.test(e))return;let s=e.match(r)[1];switch(e=e.replaceAll("/","-").replaceAll(" ","_").toLowerCase(),s){case"xml":n="data:x-application/xml;charset=utf-8,"+encodeURIComponent(t);break;case"py":n="data:text/python;charset=utf-8,"+encodeURIComponent(t);break;case"json":n="data:text/json;charset=utf-8,"+encodeURIComponent(t);break;case"csv":n="data:text/csv;charset=utf-8,"+encodeURIComponent(t);break;case"svg":n="data:image/svg+xml;charset=utf-8,"+encodeURIComponent(t);break;case"png":n=t}let a=document.createElement("a");a.setAttribute("href",n),a.setAttribute("download",e),a.style.display="none",document.body.appendChild(a),a.click(),document.body.removeChild(a)}static setSelected(e,t){for(var n=0;n<e.$.options.length;n++)if(e.$.options[n].text==t)return void(e.$.options[n].selected=!0)}static lazyUpdate(t,n,r,s){s=null==s?"innerText":s;let a=e.get(`[data-uid='${n}']`,t);for(const t in r)e.get(`#${t}`,a)[s]=r[t]}}class t{static randomChar(){const e="abcdefghijklmnopqrstuvwxyz";return e[Math.floor(26*Math.random())]}static UID(){return this.randomChar()+(+new Date).toString(36)+Math.random().toString(36).substring(3)}static SID(){return this.randomChar()+Math.random().toString(36).substring(3,8)}static fromUrl(e){let t=new URLSearchParams(document.location.search);return null==t.get(e)?this.urlDefaults(e):this.urlValidParams(e,t.get(e))}static urlDefaults(e){if("theme"===e)return"light"}static urlValidParams(e,t){if("theme"===e)return["dark","light"].includes(t)?t:this.urlDefaults(e)}static cleanPathname(e){return e.replace(/([^:]\/)\/+/g,"$1").replace(/[^:]\.\//g,"$1")}static getDepth(e){return(e.match(/\//g)||[]).length}static cache_check(e,t,n,r){let s=localStorage.getItem(t);null!==s&&(s=JSON.parse(s));let a=new Date(0);a.setHours(n),!0===e.reloaded||null===s||s.timestamp+a.valueOf()<Date.now()?fetch(t,{method:"Get",headers:{"Content-Type":"application/json"}}).then((e=>{if(!0===e.ok)return e.json()})).then((e=>{e&&(s={obj:e},s.timestamp=Date.now(),r(e),localStorage.setItem(t,JSON.stringify(s)))})).catch((e=>{console.error(`Failed to resolve ${t}, due to:`,e)})):r(s.obj)}}class n{constructor(e){this.$={},this.parent=e,this.fetch_tags()}fetch_tags(){t.cache_check(this.parent.state,`/${this.parent.state.repository}/tags.json`,2,(e=>{this.render(e)}))}assert(e){if(Array.isArray(e))return e.every((e=>"string"==typeof e))?"string-array":(console.warn("version_dropdown: expected array of strings, got ",e),!0);if("[object Object]"===Object.prototype.toString.call(e)){for(let t in e){if(!Array.isArray(e[t]))return console.warn("version_dropdown: expected array, got ",e[t]),!0;if(2!==e[t].length)return console.warn(`version_dropdown: expected two items, got ${e[t].length}`,e[t]),!0}return"fine-grained"}return console.warn("version_dropdown: expected object of arrays or array of strings, got ",e),!0}string_array_to_object(e){let t={};e.forEach((e=>{t[e]=[e,""]})),""in t&&(t[""]=["main","unstable"]);for(const e in t){t[e]=[t[e][0],"latest"];break}return t}render(t){let n=this.parent.state.version,r=this.parent.state.path,s="",a=this.assert(t);if(!0===a)return;"string-array"==a&&(t=this.string_array_to_object(t));let o=e.get(".sphinxsidebarwrapper .toc-tree"),i=e.get("header #right .reverse"),c=e.get("body"),l=Object.keys(t).length>10?4:2,p=" auto".repeat(l),h=new e("div",{className:"version-dropdown-list",style:`grid-template-columns:${p}`});t.hasOwnProperty(r)?(s=t[r][1],n=t[r][0]):console.warn(`version_dropdown: current path ${r} is not in the tags.json`,t);for(let n in t){let r=new e("a",{href:`/${this.parent.state.repository}/${n}`}),s=new e("div"),a=new e("div");s.innerText=t[n][0];let o=new e("span",{className:""===t[n][1]?"":"label"});o.innerText=t[n][1],a.append(o),r.append(s),r.append(a),h.append(r)}let d=new e("dev",{id:"cancel-area-show-version-dropdown"});c.append(d.$),c.append(h.$);let u=new e("div",{className:"version-dropdown"});u.innerText=n;let m=new e("span",{className:""===s?"":"label"});m.innerText=s,u.append(m),o.insertAdjacentElement("afterbegin",u.$);let f=new e(u.$.cloneNode(!0));u.onclick(this,this.show,[!0]),f.onclick(this,this.show,[!0]),d.onclick(this,this.show,[!0]),i.append(f.$),this.$.list=h,this.$.cancel=d}show(t){e.switchState(this.$.cancel),e.switchState(this.$.list)}}class r{constructor(e){this.$={},this.set_doms(),this.parent=e;let t=e.state.metadata;"repotoc"in t&&this.update_repotoc(t.repotoc),"banner"in t&&this.update_banner(t.banner)}set_doms(){let t=this.$;t.repotocTreeOverlay=new e(e.get(".repotoc-tree.overlay root")),t.repotocTreeSidebar=new e(e.get(".sphinxsidebar .repotoc-tree root")),t.banner=new e("div",{className:"banner"}),e.get("body").prepend(t.banner.$)}update_repotoc(t){let n=this.$,r=[],s=[];for(const[n,r]of Object.entries(t)){if(!("name"in r))continue;let t=n==this.parent.state.repository?this.parent.state.content_root:`/${n}/`;s.push(new e("a",{href:`${t}index.html`,className:this.parent.state.repository===n?"current":"",innerText:r.name}))}s.forEach((e=>{r.push(e.cloneNode(!0))})),n.repotocTreeOverlay.$&&(n.repotocTreeOverlay.removeChilds(),n.repotocTreeOverlay.append(r)),n.repotocTreeSidebar.$&&(n.repotocTreeSidebar.removeChilds(),n.repotocTreeSidebar.append(s))}update_banner(t){let n=this.$;"msg"in t&&n.banner.append(new e("span",{innerText:t.msg})),"a_href"in t&&"a_text"in t&&n.banner.append(new e("a",{href:t.a_href,innerText:t.a_text,target:"_blank"}))}}function s(){new n(app),new r(app)}return s(),s}));
//# sourceMappingURL=extra.umd.js.map
