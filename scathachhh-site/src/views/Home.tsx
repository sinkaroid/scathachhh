import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
  },
})

export default class Home extends Vue {

  private render() {

    return <div id="home">
      
          <div class="animated zoomIn">
            <img src="https://scathach.redsplit.org/src/me.png" class="img1" width="250px" />
            <br />
            
            {
            // <center>
            // <a href="https://www.codefactor.io/repository/github/redsplit/scathach">
              // <img src="https://www.codefactor.io/repository/github/redsplit/scathach/badge" alt="Scathach" />
            // </a> 

            // <a href="https://travis-ci.com/Redsplit/scathach">
              // <img src="https://travis-ci.com/Redsplit/scathach.svg?branch=master" alt="Scathach" />
            // </a>

            // <a href="https://top.gg/bot/724047481561809007">
              // <img src="https://top.gg/api/widget/servers/724047481561809007.svg" alt="Scathach" />
            // </a>
            // </center>
            }
            <h1 class="text-center text-white font-weight-bold my-1">Scathach bot.</h1>
            
            <font face="Ubuntu">
            <p class="text-center text-white my-2">
            LEWD AGGREGATOR BOT<br /><br />
            <center>

            <div id="steal" role="group">
              <a href="https://scathach.redsplit.org/bot" target="_blank" class="btn text-white waves-efect font-weight-bolder"><i class="fas fa-rocket text-white fa-lg mr-1"></i>Invite bot</a>
              <a href="https://docs.redsplit.org/" class="btn text-white waves-efect font-weight-bolder"><i class="fas fa-bug text-white fa-lg mr-1"></i>DOCS</a>
              <a href="https://www.npmjs.com/package/lewdorder" class="btn text-white waves-efect font-weight-bolder"><i class="fas fa-database text-white fa-lg mr-1"></i>API</a>
              <a href="https://docs.redsplit.org/changelogs" class="btn text-white waves-efect font-weight-bolder"><i class="fas fa-list text-white fa-lg mr-1"></i>CHANGELOGS</a>
              <a href="https://docs.redsplit.org/privacy-policy" class="btn text-white waves-efect font-weight-bolder"><i class="fas fa-lock text-white fa-lg mr-1"></i>PRIVACY POLICY</a>
            </div>
            </center><br />
    Neither a the best NSFW nor the next level bot, but it's compete!<br />No bullshit,just wholesome content: DotA 2, great NSFW content, Memes, NERDS utilities, vTuber scraper, Anime and Cryptocurrency!<br />There will also be a new and upcoming future mod commands through the bot. So, enjoy!<br />
    <br /><i>
    It's all free, forever. We’ll never make you donate - unlike bots that beg for premium.</i>
    <br /><font size="2">
    <div class="footer__row">with <span aria-label="Vue" role="img" class="material-design-icon vuejs-icon"><svg fill="currentColor" width="24" height="24" viewBox="0 0 24 24" class="material-design-icon__svg"><path d="M2,3H5.5L12,15L18.5,3H22L12,21L2,3M6.5,3H9.5L12,7.58L14.5,3H17.5L12,13.08L6.5,3Z"><title>Vue</title></path></svg></span>, <span aria-label="NodeJS" role="img" class="material-design-icon nodejs-icon"><svg fill="currentColor" width="24" height="24" viewBox="0 0 24 24" class="material-design-icon__svg"><path d="M12,1.85C11.73,1.85 11.45,1.92 11.22,2.05L3.78,6.35C3.3,6.63 3,7.15 3,7.71V16.29C3,16.85 3.3,17.37 3.78,17.65L5.73,18.77C6.68,19.23 7,19.24 7.44,19.24C8.84,19.24 9.65,18.39 9.65,16.91V8.44C9.65,8.32 9.55,8.22 9.43,8.22H8.5C8.37,8.22 8.27,8.32 8.27,8.44V16.91C8.27,17.57 7.59,18.22 6.5,17.67L4.45,16.5C4.38,16.45 4.34,16.37 4.34,16.29V7.71C4.34,7.62 4.38,7.54 4.45,7.5L11.89,3.21C11.95,3.17 12.05,3.17 12.11,3.21L19.55,7.5C19.62,7.54 19.66,7.62 19.66,7.71V16.29C19.66,16.37 19.62,16.45 19.55,16.5L12.11,20.79C12.05,20.83 11.95,20.83 11.88,20.79L10,19.65C9.92,19.62 9.84,19.61 9.79,19.64C9.26,19.94 9.16,20 8.67,20.15C8.55,20.19 8.36,20.26 8.74,20.47L11.22,21.94C11.46,22.08 11.72,22.15 12,22.15C12.28,22.15 12.54,22.08 12.78,21.94L20.22,17.65C20.7,17.37 21,16.85 21,16.29V7.71C21,7.15 20.7,6.63 20.22,6.35L12.78,2.05C12.55,1.92 12.28,1.85 12,1.85M14,8C11.88,8 10.61,8.89 10.61,10.39C10.61,12 11.87,12.47 13.91,12.67C16.34,12.91 16.53,13.27 16.53,13.75C16.53,14.58 15.86,14.93 14.3,14.93C12.32,14.93 11.9,14.44 11.75,13.46C11.73,13.36 11.64,13.28 11.53,13.28H10.57C10.45,13.28 10.36,13.37 10.36,13.5C10.36,14.74 11.04,16.24 14.3,16.24C16.65,16.24 18,15.31 18,13.69C18,12.08 16.92,11.66 14.63,11.35C12.32,11.05 12.09,10.89 12.09,10.35C12.09,9.9 12.29,9.3 14,9.3C15.5,9.3 16.09,9.63 16.32,10.66C16.34,10.76 16.43,10.83 16.53,10.83H17.5C17.55,10.83 17.61,10.81 17.65,10.76C17.69,10.72 17.72,10.66 17.7,10.6C17.56,8.82 16.38,8 14,8Z"><title>NodeJS</title></path></svg></span> and <span aria-label="love" role="img" class="material-design-icon heart-icon"><svg fill="currentColor" width="24" height="24" viewBox="0 0 24 24" class="material-design-icon__svg"><path d="M12,21.35L10.55,20.03C5.4,15.36 2,12.27 2,8.5C2,5.41 4.42,3 7.5,3C9.24,3 10.91,3.81 12,5.08C13.09,3.81 14.76,3 16.5,3C19.58,3 22,5.41 22,8.5C22,12.27 18.6,15.36 13.45,20.03L12,21.35Z"><title>love</title></path></svg></span></div>
    </font></p>

    
    </font>

          </div>
        </div>

  }

}
