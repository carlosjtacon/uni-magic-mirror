import { MirrorClientPage } from './app.po';

describe('mirror-client App', () => {
  let page: MirrorClientPage;

  beforeEach(() => {
    page = new MirrorClientPage();
  });

  it('should display welcome message', done => {
    page.navigateTo();
    page.getParagraphText()
      .then(msg => expect(msg).toEqual('Welcome to app!!'))
      .then(done, done.fail);
  });
});
