import defaultSettings from '@/settings'

const title = defaultSettings.title || 'Automatic Segmentation System Of Hippocampus'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
