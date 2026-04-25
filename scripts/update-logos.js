const fs = require('fs');

const newLogoUrl = 'https://hebbkx1anhila5yf.public.blob.vercel-storage.com/204C03A2-6C9F-460C-8EE4-55C05559832C.PNG-4MCtBhXB9bL3SoX1Zx2pnWqAsj4OPf.png';
const files = ['/vercel/share/v0-project/KATRACO-RWANDA.html', '/vercel/share/v0-project/index.html'];

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  
  // Replace the nav and footer logos
  const baseImagePattern = /src="data:image\/jpeg;base64,[^"]*"/g;
  content = content.replace(baseImagePattern, `src="${newLogoUrl}" alt="KATRACO Rwanda Logo"`);
  
  fs.writeFileSync(file, content);
  console.log(`Updated ${file}`);
});
